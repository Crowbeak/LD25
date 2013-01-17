#TODO: Create site class, which is a collection of Workplace instances.
#TODO: Make constants variables for each workplace,
#      initialized once like average downtime.
#TODO: Add simulation class which holds the simulation game state variables,
#      including simulation name and phase.
#TODO: Check for and get rid of unused modules.


###############################################################################
# Imports and Initializations
###############################################################################
import random

random.seed()


FARM_BASE = 3.0
FARM_UTIL_RATIO = 0.05
FACTORY_BASE = 10.0
FACTORY_STR_RATIO = 0.03
BREAKDOWN_RATIO = 0.005
BROKEN_BEFORE = 0.001


###############################################################################
# Exceptions
###############################################################################
class TooManyRobots(Exception):
    """
    TooManyRobots is raised by Workplace instances when adding another robot
    would result in the max number of robots for that Workplace being exceeded.
    """


###############################################################################
# Labor Robot Class
###############################################################################
class LaborRobot(object):
    def __init__(self, id, age, strength, battery, utility, cost, breakdowns=0,
                 output=0):
        """
        id: ID number for robot (a positive int).
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
        
        """
        TODO: Delete this docstring.
              Saved for reference until all changes verified.
        
        self.id = id
        self.age = age
        self.str = strength
        self.batt = battery
        self.util = utility
        self.cost = cost
        self.breaks = breakdowns
        self.out = output
        """
        self.id = id
        self.age = age
        self.strength = strength
        self.battery = battery
        self.utility = utility
        self.cost = cost
        self.breakdowns = breakdowns
        self.output = output
    
    def breakdownProb(self):
        """
        Returns probability of the robot breaking down in a week (a float).
        """
        if self.age <= 1:
            return BREAKDOWN_RATIO + (self.breakdowns*BROKEN_BEFORE)
        else:
            return (self.age*BREAKDOWN_RATIO) + (self.breakdowns*BROKEN_BEFORE)
    
    def incrementBreaks(self):
        self.breakdowns += 1
    
    def addOutput(self, amount):
        self.output += amount


###############################################################################
# Workplace Classes
#   Includes basic Workplace definition and subclasses.
###############################################################################
class Workplace(object):
    """
    Representation of work environment for robots.
    """
    def __init__(self, maxRobots, avgDowntime, robots = []):
        """
        maxRobots: Maximum number of robots the place can hold (a non-neg int).
        avgDowntime: Average time to repair a robot, in days (int between 1-7).
        robots: A list of robot objects currently at the workplace.
        """
        
        """
        TODO: Delete this docstring.
              Saved for reference until all changes complete.
              
        self.max = maxRobots
        self.down = avgDowntime
        self.curr = currentRobots
        """
        self.maxRobots = maxRobots
        self.avgDowntime = avgDowntime
        self.robots = robots
    
    def addRobot(self, robot):
        """
        Adds a robot to the list of currentRobots.
        """
        if len(self.robots) < self.maxRobots:
            self.robots.append(robot)
        else:
            raise TooManyRobots("Max number of robots exceeded.")
    
    def removeRobot(self, id):
        """
        Pops the robot with the given id number from the list of currentRobots
        if the robot is in the list.
        #TODO: Otherwise, raise exception.
        """
        for i in range(len(self.robots)):
            if self.robots[i].id == id:
                return self.robots.pop(i)
    
    def getTotalOutput(self):
        """
        Returns the total output of all robots at the workplace.
        """
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


class Unassigned(Workplace):
    """
    Placeholder for robots not yet assigned to a real workplace.
    """
    def __init__(self, robots = []):
        self.robots = robots
        self.maxRobots = None   #Need for pDisplayWorkplace.
    
    def addRobot(self, robot):
        self.robots.append(robot)


class Farm(Workplace):
    """
    Representation of a farm where robots work.
    """
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks for that robot.
        """
        for robot in self.robots:
            if random.random() < robot.breakdownProb():
                robot.incrementBreaks()
                output = int(((robot.strength*FARM_BASE) * robot.battery *
                             (7-self.avgDowntime) * (robot.utility*FARM_UTIL_RATIO)))
            else:
                output = int(((robot.strength*FARM_BASE) * robot.battery * 7 *
                             (robot.utility*FARM_UTIL_RATIO)))
            robot.addOutput(output)
        

class Factory(Workplace):
    """
    Representation of a factory where robots work.
    """
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks for that robot.
        """
        for robot in self.robots:
            if random.random() < robot.breakdownProb():
                robot.incrementBreaks()
                output = int(((robot.utility*FACTORY_BASE) * robot.battery *
                             (7-self.avgDowntime) * (robot.strength*FACTORY_STR_RATIO)))
            else:
                output = int(((robot.utility*FACTORY_BASE) * robot.battery * 7 *
                             (robot.strength*FACTORY_STR_RATIO)))
            robot.addOutput(output)