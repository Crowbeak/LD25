import pyglet

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

ch01_desk = pyglet.resource.image('img/desk.png')

everyday_bgm = pyglet.resource.media('music/bgm01.mp3')