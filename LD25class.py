#TODO: Turn constants into randomized functions AND/OR
#      balance them for specific sims (difficulty scaling).

import random

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
# Labor Robot Class
###############################################################################
class LaborRobot(object):
    def __init__(self, id, age, strength, battery, utility, cost, breakdowns=0,
                 output=0):
        """
        age: Number of years robot has been in service (a non-negative int).
        strength: Tens of pounds the robot can carry (a positive float).
        battery: Average battery life of the robot in hours (a non-negative
                 float).
        utility: Rating of robot's ability to complete varying kinds of
                 tasks (an integer between 1-10).
        cost: Average weekly cost in resources to maintain the robot (a non-
              negative int).
        breakdowns: Total number of times the robot has broken down (a non-
                    negative int).
        output: Total resource output (a non-negative int).
        """
        self.id = id
        self.age = age
        self.strength = strength
        self.battery = battery
        self.utility = utility
        self.cost = cost
        self.breakdowns = breakdowns
        self.output = output
        self.BREAKDOWN_RATIO = 0.005
        self.BROKEN_BEFORE = 0.001
    
    def breakdownProb(self):
        """
        Returns probability of the robot breaking down during a week (a float).
        """
        if self.age <= 1:
            return self.BREAKDOWN_RATIO + (self.breakdowns*self.BROKEN_BEFORE)
        else:
            return ((self.age*self.BREAKDOWN_RATIO) +
                    (self.breakdowns*self.BROKEN_BEFORE))

    #TODO: Make following modules into properties?
    def incrementBreaks(self):
        self.breakdowns += 1
    
    def addOutput(self, amount):
        self.output += amount


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
        self.robots = robots
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
        self.FARM_BASE = 3.0
        self.FARM_UTIL_RATIO = 0.05
    
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks for that robot.
        """
        for robot in self.robots:
            if random.random() < robot.breakdownProb():
                robot.incrementBreaks()
                output = int(((robot.strength*self.FARM_BASE) * robot.battery *
                             (7-self.avgDowntime) *
                             (robot.utility*self.FARM_UTIL_RATIO)))
            else:
                output = int(((robot.strength*self.FARM_BASE) * robot.battery *
                             7 * (robot.utility*self.FARM_UTIL_RATIO)))
            robot.addOutput(output)
        

class Factory(Workplace):
    def __init__(self, maxRobots, robots=[], name="FACTORY", cmd="FACT"):
        """
        cmd: console command for robot placement phase (a 4-character uppercase
             string).
        """
        Workplace.__init__(self, maxRobots, robots, name, cmd)
        self.FACTORY_BASE = 10.0
        self.FACTORY_STR_RATIO = 0.03
        
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks for that robot.
        """
        for robot in self.robots:
            if random.random() < robot.breakdownProb():
                robot.incrementBreaks()
                output = int(((robot.utility*self.FACTORY_BASE) *
                             robot.battery * (7-self.avgDowntime) *
                             (robot.strength*self.FACTORY_STR_RATIO)))
            else:
                output = int(((robot.utility*self.FACTORY_BASE) *
                             robot.battery * 7 *
                             (robot.strength*self.FACTORY_STR_RATIO)))
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


###############################################################################
# Simulation State Class
###############################################################################
class SimState(object):
    """
    Represents the state of the simulation at any given time.
    """
    def __init__(self, robotsToDiscardNum, workplaces=[], name="SIMULATION",
                 weeks=104):
        """
        workplaces: A list of Workplace objects.
        phase: current phase of simulation (a string).
        """
        self.robotsToDiscardNum = robotsToDiscardNum
        self.workplaces = workplaces[:]
        self.name = name
        self.weeks = weeks
        self.phase = "ROBOT PLACEMENT"