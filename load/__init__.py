import pyglet

class StaticImage(pyglet.sprite.Sprite):
    """
    Creates an instance of an unmoving image.
    """
    def __init__(self, *args, **kwargs):
        super(StaticImage, self).__init__(*args, **kwargs)
        self.dead = False
    
    def die(self, dt):
        self.dead = True

class TimedImage(StaticImage):
    """
    Creates an instance of an unmoving foreground image which will cease to
    be after a certain amount of time.
    """
    def __init__(self, death_timer=None, *args, **kwargs):
        super(TimedImage, self).__init__(*args, **kwargs)
        if death_timer is not None:
            pyglet.clock.schedule_once(self.die, death_timer)

class StaticText(pyglet.text.Label):
    """
    Creates a text label to be displayed onscreen.
    """
    def __init__(self, *args, **kwargs):
        super(StaticText, self).__init__(color=(0, 0, 0, 255), multiline=True,
                                         width=500, *args, **kwargs)
        self.dead = False
    
    def die(self, dt):
        self.dead = True

class ComputerText(StaticText):
    """
    Creates a text label to be displayed on the computer screen in the player's
    cubicle.
    """
    def __init__(self, *args, **kwargs):
        super(ComputerText, self).__init__(width=500, x=150, y=485,
                                           *args, **kwargs)