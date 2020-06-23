import pyxel
from player import Player

width = 128
height = 128
#init(width, height, [caption], [scale], [palette], [fps], [quit_key], [fullscreen])
pyxel.init(width, height, caption="invader", scale=4,
           fps=30, quit_key=pyxel.KEY_ESCAPE)
pyxel.load("my_resource.pyxres")

player = Player(width, height)


def update():
    player.update(width, height)


def draw():
    pyxel.cls(0)
    player.draw()


pyxel.run(update, draw)
