import pyglet

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

#TODO: Use this.
def _center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

#Backgrounds
blank_bg = pyglet.resource.image('img/blank.png')
ch01_desk = pyglet.resource.image('img/desk.png')

#Musics
everyday_bgm = pyglet.resource.media('music/bgm01.ogg')

#Title Resources
title_pic = pyglet.resource.image('img/title.png')
lena_pic = pyglet.resource.image('img/feet.png')
seal_pic = pyglet.resource.image('img/country_seal.png')

title_pic.anchor_x = title_pic.width
lena_pic.anchor_x = lena_pic.width
seal_pic.anchor_x, anchor_y = seal_pic.width/2, seal_pic.height