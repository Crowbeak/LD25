import random

random.seed()

FARM_BASE = 10.0
FARM_UTIL_RATIO = 0.05
FACTORY_BASE = 10.0
FACTORY_STR_RATIO = 0.3
BREAKDOWN_RATIO = 0.01

class LaborRobot(object):
    """
    Representation of a labor robot.
    """
    def __init__(self, age, strength, battery, utility, cost, breakdowns = 0, output=0):
        """
        Initializes a LaborRobot instance, saves all parameters as attributes
        of the instance.
        
        age: Number of years robot has been in service (a non-negative int).
        strength: Tens of pounds the robot can carry (a non-negative float).
        battery: Average battery life of the robot in hours (a non-negative
                 float).
        utility: Rating of robot's ability to complete varying kinds of
                 tasks (an integer between 1-10).
        cost: Average weekly cost in resources to maintain the robot (a non-
              negative int).
        output: Total resource output (a non-negative int).
        breakdowns: Total number of times the robot has broken down (a non-
                    negative int).
        """
        self.age = age
        self.str = strength
        self.batt = battery
        self.util = utility
        self.cost = cost
        self.out = output
        self.breaks = breakdowns
    
    def farmOutput(self):
        """
        Returns the number of resources produced in a week working farmland.
        """
        return ((self.str*FARM_BASE) * (self.batt/24) * 7 *
                (self.util*FARM_UTIL_RATIO))
    
    def factoryOutput(self):
        """
        Returns the number of resources produced in a week working a factory.
        """
        return ((self.util*FACTORY_BASE) * (self.batt/24) * 7 *
                (self.str*FACTORY_STR_RATIO))
    
    def breakdown(self):
        """
        Returns probability of the robot breaking down in a week (a float).
        """
        return self.age * BREAKDOWN_RATIO
    
    def incBreak(self):
        """
        Increments the robot's number of breakdowns.
        """
        self.breaks += 1
    
    def addOut(self, amount):
        """
        Adds to the robot's total output.
        """
        self.out += amount
    
    def cost(self):
        """
        Returns the average weekly cost to maintain the robot.
        """
        return self.cost
    
    def output(self):
        """
        Returns the robot's total output.
        """
        return self.out
    
    def stats(self):
        """
        Returns all of the robots's stats.
        """
        return (self.age, self.str, self.batt, self.util, self.cost,
                self.out, self.breaks)

class Workplace(object):
    """
    Representation of work environment for robots.
    """
    def __init__(self, maxRobots, repairCost, avgDowntime, currentRobots = []):
        """
        Initializes a Workplace instance, saves all parameters as attributes
        of the instance.
        
        maxRobots: Maximum number of robots the place can hold (a non-neg int).
        repairCost: Average cost to repair a broken robot in resources (a non-
                    negative int).
        avgDowntime: Average time to repair a robot, in days (int between 1-7).
        currentRobots: A list of robot objects currently at the workplace.
        """
        self.max = maxRobots
        self.repair = repairCost
        self.down = avgDowntime
        self.curr = currentRobots
    
    def add(self, robot):
        """
        Adds a robot to the list of currentRobots.
        """
        self.curr.append(robot)
    
    def remove(self, robot):
        """
        Pops the given robot from the list of currentRobots.
        """
        for i in len(self.curr):
            if self.curr[i] is robot:
                self.curr.pop(i)
    
    def totalOut(self):
        """
        Returns the total output at the workplace.
        """
        temp = 0
        for robot in self.curr:
            temp += robot.out
        
        return temp
        
    def totalCost(self):
        """
        Returns the total cost of robot maintenance at the workplace.
        """
        temp = 0
        for robot in self.curr:
            temp += robot.cost
        
        return temp
    
    def avgOut(self):
        """
        Returns the average weekly output per robot as a float.
        """
        return self.totalOut()/float(len(self.curr))
    
    def avgCost(self):
        """
        Returns the average weekly cost to maintain a robot at the workplace.
        """
        return self.totalCost()/float(len(self.curr))

class Farm(Workplace):
    """
    Representation of a farm where robots work.
    """
    pass

class Factory(Workplace):
    """
    Representation of a factory where robots work.
    """
    pass