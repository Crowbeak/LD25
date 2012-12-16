#TODO: Create site class, which is a collection of Workplace instances.
#TODO: Make constants variables for each workplace,
#      initialized once like average downtime.

import random

random.seed(0)


FARM_BASE = 3.0
FARM_UTIL_RATIO = 0.05
FACTORY_BASE = 10.0
FACTORY_STR_RATIO = 0.03
BREAKDOWN_RATIO = 0.005
BROKEN_BEFORE = 0.001


class LaborRobot(object):
    """
    Representation of a labor robot.
    """
    def __init__(self, id, age, strength, battery, utility, cost, breakdowns=0,
                 output=0):
        """
        Initializes a LaborRobot instance, saves all parameters as attributes
        of the instance.
        
        id: ID number for robot (a positive int).
        age: Number of years robot has been in service (a non-negative int).
        strength: Tens of pounds the robot can carry (a positive float).
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
        self.id = id
        self.age = age
        self.str = strength
        self.batt = battery
        self.util = utility
        self.cost = cost
        self.breaks = breakdowns
        self.out = output
    
    def strength(self):
        """
        Returns robot's strength.
        """
        return self.str
    
    def battery(self):
        """
        Returns robot's battery life.
        """
        return self.batt

    def utility(self):
        """
        Returns robot's utility rating.
        """
        return self.util
    
    def idNum(self):
        """
        Returns robot's ID number.
        """
        return self.id
    
    def breakdown(self):
        """
        Returns probability of the robot breaking down in a week (a float).
        """
        if self.age <= 1:
            return BREAKDOWN_RATIO + (self.breaks*BROKEN_BEFORE)
        else:
            return (self.age*BREAKDOWN_RATIO) + (self.breaks*BROKEN_BEFORE)
    
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
    
    def costs(self):
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
        return (self. id, self.age, self.str, self.batt, self.util, self.cost,
                self.breaks, self.out)
           
                
class TooManyRobots(Exception):
    """
    TooManyRobots is raised by all Workplace instances when adding another robot
    would result in the max number of robots for that Workplace being exceeded.
    """


class Workplace(object):
    """
    Representation of work environment for robots.
    """
    def __init__(self, maxRobots, avgDowntime, currentRobots = []):
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
        self.down = avgDowntime
        self.curr = currentRobots
    
    def addRobo(self, robot):
        """
        Adds a robot to the list of currentRobots.
        """
        if len(self.curr) < self.max:
            self.curr.append(robot)
        else:
            raise TooManyRobots("Max number of robots exceeded.")
    
    def rem(self, id):
        """
        Pops a robot from the list of currentRobots.
        """
        for i in range(len(self.curr)):
            if self.curr[i].id == id:
                return self.curr.pop(i)
    
    def robots(self):
        """
        Returns the list of current robots.
        """
        return self.curr
    
    def getMax(self):
        """
        Returns the maximum number of robots the workplace can hold.
        """
        return self.max
    
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
    
    def avgOut(self, weeks):
        """
        Returns the average weekly output per robot as a float.
        """
        return (self.totalOut()/weeks)/float(len(self.curr))
    
    def avgCost(self):
        """
        Returns the average weekly cost to maintain a robot at the workplace.
        """
        return self.totalCost()/float(len(self.curr))


class Unassigned(Workplace):
    """
    Handler for robots not yet assigned to a real workplace.
    """
    def __init__(self, robots):
        self.curr = robots
        self.max = None
    
    def addRobo(self, robot):
        self.curr.append(robot)


class Farm(Workplace):
    """
    Representation of a farm where robots work.
    """
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks.
        """
        for robot in self.curr:
            if random.random() < robot.breakdown():
                robot.incBreak()
                output = int(((robot.str*FARM_BASE) * robot.batt *
                             (7-self.down) * (robot.util*FARM_UTIL_RATIO)))
            else:
                output = int(((robot.str*FARM_BASE) * robot.batt * 7 *
                             (robot.util*FARM_UTIL_RATIO)))
            robot.addOut(output)
        

class Factory(Workplace):
    """
    Representation of a factory where robots work.
    """
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks.
        """
        for robot in self.curr:
            if random.random() < robot.breakdown():
                robot.incBreak()
                output = int(((robot.util*FACTORY_BASE) * robot.batt *
                             (7-self.down) * (robot.str*FACTORY_STR_RATIO)))
            else:
                output = int(((robot.util*FACTORY_BASE) * robot.batt * 7 *
                             (robot.str*FACTORY_STR_RATIO)))
            robot.addOut(output)