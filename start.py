import pyglet

from story import *
from classes import WindowState

game_window = WindowState()

"""
player = pyglet.media.Player()
player.queue(resources.everyday_bgm)
player.eos_action = player.EOS_LOOP
player.play()
"""

def update(dt):
    pass

@game_window.window.event
def on_draw():
    game_window.window.clear()
    #game_window.bg_batch.draw()
    #game_window.fg_batch.draw()
    game_window.text_batch.draw()
    

def main():
    title(game_window)
    #intro()
    #ch01()
    #dave = ch02()
    #ch03(dave)
    #spanishInquisition()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
    main()
