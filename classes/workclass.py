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
    _avg_downtime = random.randint(1, 7)
    
    def __init__(self, max_robots, robots=[], name="WORKPLACE", cmd="WORK"):
        """
        max_obots: Maximum number of robots the place can hold (a non-neg int).
        avgDowntime: Average time to repair a robot, in days (int between 1-7).
        cmd: console command for robot placement phase (a 4-character uppercase
             string).
        """
        self.max_robots = max_robots
        self.robots = copy.deepcopy(robots)
        self.name = name
        self.cmd = cmd
    
    def add_robot(self, robot):
        if len(self.robots) < self.max_robots:
            self.robots.append(robot)
        else:
            raise TooManyRobots("Max number of robots exceeded.")
    
    def removeRobot(self, id):
        #TODO: Otherwise, raise exception.
        for i in range(len(self.robots)):
            if self.robots[i].id == id:
                return self.robots.pop(i)
    
    def total_output(self):
        total = 0
        for robot in self.robots:
            total += robot.total_output
        
        return total
    
    def avg_output(self, weeks):
        """
        Returns the average weekly output per robot as a float.
        """
        return (self.total_output()/weeks)/float(len(self.robots))
    
    def update(self):
        raise NotImplemented("Module update() not implemented.")


class Unassigned(Workplace):
    """
    Placeholder for robots not yet assigned to an actual workplace.
    """
    def add_robot(self, robot):
        self.robots.append(robot)
    
    def update(self):
        pass


class Farm(Workplace):
    """
    Instance of a farm workplace type.
    """
    _major_stat_ratio = 3.0
    _minor_stat_ratio = 0.05
    
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks for that robot.
        """
        for robot in self.robots:
            if random.random() < robot.breakdown_prob():
                robot.breakdowns += 1
                output = int(((robot.strength*self._major_stat_ratio) *
                             robot.battery * (7-self._avg_downtime) *
                             (robot.utility*self._minor_stat_ratio)))
            else:
                output = int(((robot.strength*self._major_stat_ratio) *
                             robot.battery * 7 *
                             (robot.utility*self._minor_stat_ratio)))
            robot.total_output += output
        

class Factory(Workplace):
    _major_stat_ratio = 10.0
    _minor_stat_ratio = 0.03
        
    def update(self):
        """
        Updates all robots' output totals after a week's worth of work.
        If a robot breaks, increments the number of breaks for that robot.
        """
        for robot in self.robots:
            if random.random() < robot.breakdown_prob():
                robot.breakdowns += 1
                output = int(((robot.utility*self._major_stat_ratio) *
                             robot.battery * (7-self._avg_downtime) *
                             (robot.strength*self._minor_stat_ratio)))
            else:
                output = int(((robot.utility*self._major_stat_ratio) *
                             robot.battery * 7 *
                             (robot.strength*self._minor_stat_ratio)))
            robot.total_output += output


###############################################################################
# Workplace Instantiator Class
###############################################################################
class WorkplaceToBe(object):
    """
    Passed to simulation for use in workplace initiation.
    
    Allows for control of simulation balance, but with variability from
    randomization each time.
    """
    breakdown_chance = [0, 0, 0, 0, 1, 1, 1, 2, 2, 3]
    
    def __init__(self, number_of_robots, robots_are_old, constructor, name, cmd):
        self.number_of_robots = number_of_robots
        self.robots_are_old = robots_are_old
        self.constructor = constructor
        self.name = name
        self.cmd = cmd