import pyxel


class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 16

    def update(self, x, y):
        self.x += x
        self.y += y

    def draw(self, kind):
        pyxel.blt(self.x, self.y, 1, 16*kind, 0, 16, 16, 0)
