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