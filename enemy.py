import pyxel


class Enemy:

    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.isAlive = True

    def update(self, x, y):
        self.x += x
        self.y += y

    def draw(self, size):
        if self.isAlive:
            pyxel.blt(self.x, self.y, 1, size*self.kind, 0, size, size, 0)

    def getPos(self):
        return {"x": self.x, "y": self.y}

    def death(self):
        self.isAlive = False
