import pyxel
from player import Player
from enemyCrowd import EnemyCrowd

PANEL_WIDTH = 128
PANEL_HEIGHT = 128

pyxel.init(PANEL_WIDTH, PANEL_HEIGHT, caption="outvader", scale=4,
           fps=30, quit_key=pyxel.KEY_ESCAPE)
pyxel.load("my_resource.pyxres")

player = Player(PANEL_WIDTH, PANEL_HEIGHT)
enemyCrowd = EnemyCrowd(0, 10)


def update():
    player.update(PANEL_WIDTH, PANEL_HEIGHT)
    enemyCrowd.update(PANEL_WIDTH, PANEL_HEIGHT, 5)
    for enemyLine in enemyCrowd.enemyList:
        for enemySingle in enemyLine:
            if enemySingle.isAlive:
                if player.isHitJudgeShot(enemySingle.x, enemySingle.y, enemyCrowd.singleSize):
                    enemySingle.death()

    if enemyCrowd.isHitJudgeShot(player.x, player.y, player.size):
        player.death()


def draw():
    pyxel.cls(0)
    player.draw()
    enemyCrowd.draw()


pyxel.run(update, draw)
