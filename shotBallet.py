import pyxel
from shot import Shot


class ShotBallet:

    def __init__(self, shotmy, shotMax, intervalMax):
        self.cooltime = -1
        self.intervalMax = intervalMax
        self.shotmy = shotmy
        self.shotList = [Shot(4) for i in range(shotMax)]  # 弾の集団

    def searchFreeShot(self):
        '''
        今動いていない弾を見つけ、インデックスを取得
        '''
        for shoti in range(len(self.shotList)):
            if self.shotList[shoti].isJudgeAlive() == False:
                return shoti
        # 全て動いている状態だと-1を返す
        return -1

    def init(self, x, y):
        '''
        空いている弾を探して初期化
        '''
        freei = self.searchFreeShot()
        if freei != -1 and self.cooltime == -1:
            self.cooltime = 0
            self.shotList[freei].init(x, y)

    def isHitShot(self, dx, dy, rangew, rangeh):
        '''
        生存している全弾の当たり判定
        '''
        for shotSingle in self.shotList:
            if shotSingle.isJudgeAlive():
                if shotSingle.isJudgeHit(dx, dy, rangew, rangeh):
                    return True  # あたっていればTrue

    def update(self, panelh):
        '''
        動作
        '''
        for shotSingle in self.shotList:
            shotSingle.update(self.shotmy, 0, panelh)

        if self.cooltime != -1:
            self.cooltime += 1
            if self.cooltime == self.intervalMax:
                self.cooltime = -1

    def draw(self):
        for shotSingle in self.shotList:
            shotSingle.draw()
