import copy

import pyglet

from load import *
from load import resources


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


class WindowState(object):
    """
    Holds variables needed for running the pyglet graphics engine.
    """
    def __init__(self):
        self.window = pyglet.window.Window(800, 600)
        self.window.set_caption("Decommissioner")

        self.bg_batch = pyglet.graphics.Batch()
        self.fg_batch = pyglet.graphics.Batch()
        self.text_batch = pyglet.graphics.Batch()

        self.bg = StaticImage(img=resources.ch01_desk, batch=self.bg_batch)
        self.text = StaticText("Testing, bitches!", batch=self.text_batch)