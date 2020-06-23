import pyxel


class Shot:

    def __init__(self, size):
        self.size = size
        self.isAlive = False

    def init(self, x, y):
        self.x = x
        self.y = y
        self.isAlive = True

    def isJudgeAlive(self):
        return self.isAlive

    def update(self, my, panelh):
        if(self.isAlive):
            self.y += my

        if self.y > panelh:
            self.isAlive = False

    def draw(self):
        pyxel.rect(self.x, self.y, self.size, self.size, 255)
