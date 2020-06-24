import pyxel


class Shot:

    def __init__(self, size):
        self.size = size
        self.isAlive = False

    def init(self, x, y):
        self.x = x - self.size/2
        self.y = y
        self.isAlive = True

    def isJudgeAlive(self):
        return self.isAlive

    def isJudgeHit(self, dx, dy, rangew, rangeh):
        # 三平方の定理より
        # (弾の距離とオブジェクトの距離)の2乗が
        # (弾のサイズとオブジェクトのサイズ)の2乗以内ならHIT
        if (dx - self.x)**2 + (dy - self.y)**2 \
                <= (rangew/2 + self.size/2) ** 2 + (rangeh/2 + self.size/2) ** 2:
            return True

        return False

    def update(self, my, topy, bottomy):
        if(self.isAlive):
            self.y += my
            if self.y < topy or self.y > bottomy:
                self.isAlive = False

    def draw(self):
        if self.isAlive:
            pyxel.rect(self.x, self.y, self.size, self.size, pyxel.COLOR_WHITE)
