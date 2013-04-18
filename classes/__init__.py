import copy

###############################################################################
# Simulation State Class
###############################################################################
class SimState(object):
    """
    Represents the state of the simulation at any given time.
    """
    def __init__(self, robots_to_discard_num, workplaces=[], name="SIMULATION",
                 weeks=104):
        """
        workplaces: A list of Workplace objects.
        phase: current phase of simulation (a string).
        """
        self.robots_to_discard_num = robots_to_discard_num
        self.workplaces = copy.deepcopy(workplaces)
        self.name = name
        self.weeks = weeks
        self.phase = "ROBOT PLACEMENT"