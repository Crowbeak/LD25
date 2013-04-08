import copy

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
        self.workplaces = copy.deepcopy(workplaces)
        self.name = name
        self.weeks = weeks
        self.phase = "ROBOT PLACEMENT"
        

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