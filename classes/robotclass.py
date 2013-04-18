###############################################################################
# Labor Robot Class
###############################################################################
class LaborRobot(object):
    """
    Instance of a labor robot.
    """
    
    _breakdown_ratio = 0.005
    _broken_before = 0.001
    total_output = 0
    
    def __init__(self, id, age, strength, battery, utility, cost,
                 breakdowns=0):
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

    def breakdown_prob(self):
        """
        Returns probability of the robot breaking down during a week (a float).
        """
        if self.age <= 1:
            return self._breakdown_ratio + (self.breakdowns*self._broken_before)
        else:
            return ((self.age*self._breakdown_ratio) +
                    (self.breakdowns*self._broken_before))