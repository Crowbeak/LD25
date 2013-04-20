import pyglet

from story import *
from load import resources

game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()

bg = pyglet.sprite.Sprite(img=resources.ch01_desk, batch=main_batch)

player = pyglet.media.Player()
player.queue(resources.everyday_bgm)
player.eos_action = player.EOS_LOOP
player.play()

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def main():
    intro()
    ch01()
    dave = ch02()
    ch03(dave)
    spanishInquisition()
    

if __name__ == '__main__':
    #main()
    
    pyglet.app.run()
