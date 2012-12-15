import pyglet

def BGM01():
    bgm = pyglet.resource.media('LD25BGM01.mp3')
    music = pyglet.media.Player()
    music.queue(bgm)
    music.eos_action = "loop"
    music.play()

    pyglet.app.run()