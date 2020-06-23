import pyxel
from player import Player
from enemyCrowd import EnemyCrowd

PANEL_WIDTH = 128
PANEL_HEIGHT = 128

#init(width, height, [caption], [scale], [palette], [fps], [quit_key], [fullscreen])
pyxel.init(PANEL_WIDTH, PANEL_HEIGHT, caption="invader", scale=4,
           fps=30, quit_key=pyxel.KEY_ESCAPE)
pyxel.load("my_resource.pyxres")

player = Player(PANEL_WIDTH, PANEL_HEIGHT)
enemyCrowd = EnemyCrowd()


def update():
    player.update(PANEL_WIDTH, PANEL_HEIGHT)
    enemyCrowd.update(PANEL_WIDTH, PANEL_HEIGHT, 5)


def draw():
    pyxel.cls(0)
    player.draw()
    enemyCrowd.draw()


pyxel.run(update, draw)
