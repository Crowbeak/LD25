#TODO: Turn constants into randomized functions AND/OR
#      balance them for specific sims (difficulty scaling).

import random
import copy

random.seed()


###############################################################################
# Exceptions
###############################################################################
class TooManyRobots(Exception):
    """
    Raised by Workplace instances when adding another robot would result in the
    max number of robots for that Workplace being exceeded.
    """

class NotImplemented(Exception):
    """
    Raised by Workplace subclass instances if the subclass has no update
    function implemented.
    """


###############################################################################
# Workplace Classes
###############################################################################
class Workplace(object):
    """
    Basic representation of work environment for robots.
    Designed to be inherited.
    """
    def __init__(self, maxRobots, robots=[], name="WORKPLACE", cmd="WORK"):
        """
        maxRobots: Maximum number of robots the place can hold (a non-neg int).
        avgDowntime: Average time to repair a robot, in days (int between 1-7).
        cmd: console command for robot placement phase (a 4-character uppercase
             string).
        """
        self.maxRobots = maxRobots
        self.robots = copy.deepcopy(robots)
        self.name = name
        self.cmd = cmd
        self.avgDowntime = random.randint(1, 7)
    
    def addRobot(self, robot):
        if len(self.robots) < self.maxRobots:
            self.robots.append(robot)
        else:
            raise TooManyRobots("Max number of robots exceeded.")
    
    def removeRobot(self, id):
        #TODO: Otherwise, raise exception.
        for i in range(len(self.robots)):
            if self.robots[i].id == id:
                return self.robots.pop(i)
    
    def getTotalOutput(self):
        total = 0
        for robot in self.robots:
            total += robot.output
        
        return total
    
    #TODO: Am I using this, or does it need to go?
    def getTotalCost(self):
        total = 0
        for robot in self.robots:
            total += robot.cost
        
        return total
    
    def getAvgOutput(self, weeks):
        """
        Returns the average weekly output per robot as a float.
        """
        return (self.getTotalOutput()/weeks)/float(len(self.robots))
    
    #TODO: Am I using this, or does it need to go?
    def getAvgCost(self):
        """
        Returns the average weekly cost to maintain a robot at the workplace
        as a float.
        """
        return self.getTotalCost()/float(len(self.robots))
    
    def update(self):
        raise NotImplemented("Module update() not implemented.")


class Unassigned(Workplace):
    """
    Placeholder for robots not yet assigned to an actual workplace.
    """
    def addRobot(self, robot):
        self.robots.append(robot)
    
    def update(self):
        pass


class Farm(Workplace):
    def __init__(self, maxRobots, robots=[], name="FARM", cmd="FARM"):
        """
        cmd: console command for robot placement phase (a 4-character uppercase
             string).
        """
        Workplace.__init__(self, maxRobots, robots, name, cmd)
        self.MAJOR_STAT_RATIO = 3.0
        self.MINOR_STAT_RATIO = 0.05
    
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks for that robot.
        """
        for robot in self.robots:
            if random.random() < robot.breakdownProb():
                robot.incrementBreaks()
                output = int(((robot.strength*self.MAJOR_STAT_RATIO) *
                             robot.battery * (7-self.avgDowntime) *
                             (robot.utility*self.MINOR_STAT_RATIO)))
            else:
                output = int(((robot.strength*self.MAJOR_STAT_RATIO) *
                             robot.battery * 7 *
                             (robot.utility*self.MINOR_STAT_RATIO)))
            robot.addOutput(output)
        

class Factory(Workplace):
    def __init__(self, maxRobots, robots=[], name="FACTORY", cmd="FACT"):
        """
        cmd: console command for robot placement phase (a 4-character uppercase
             string).
        """
        Workplace.__init__(self, maxRobots, robots, name, cmd)
        self.MAJOR_STAT_RATIO = 10.0
        self.MINOR_STAT_RATIO = 0.03
        
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks for that robot.
        """
        for robot in self.robots:
            if random.random() < robot.breakdownProb():
                robot.incrementBreaks()
                output = int(((robot.utility*self.MAJOR_STAT_RATIO) *
                             robot.battery * (7-self.avgDowntime) *
                             (robot.strength*self.MINOR_STAT_RATIO)))
            else:
                output = int(((robot.utility*self.MAJOR_STAT_RATIO) *
                             robot.battery * 7 *
                             (robot.strength*self.MINOR_STAT_RATIO)))
            robot.addOutput(output)


###############################################################################
# Workplace Instantiator Class
###############################################################################
class WorkplaceToBe(object):
    """
    Passed to simulation for use in workplace initiation.
    
    Allows for control of simulation balance, but with variability from
    randomization each time.
    """
    def __init__(self, numberOfRobots, robotsAreOld, constructor, name, cmd):
        self.numberOfRobots = numberOfRobots
        self.robotsAreOld = robotsAreOld
        self.constructor = constructor
        self.name = name
        self.cmd = cmd