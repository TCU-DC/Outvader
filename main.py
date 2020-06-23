import pyxel
from player import Player

width = 128
height = 128
#init(width, height, [caption], [scale], [palette], [fps], [quit_key], [fullscreen])
pyxel.init(width, height, caption="invader", scale=4, fps=30)
pyxel.load("my_resource.pyxres")

player = Player(width, height)


def update():
    player.update(width, height)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw():
    pyxel.cls(0)
    player.draw()


pyxel.run(update, draw)
