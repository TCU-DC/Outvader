import pyxel
from shot import Shot


class ShotBallet:

    def __init__(self, showMax):
        self.shotmy = 5
        self.shotList = [Shot() for i in showMax]  # 弾の集団

    def searchFreeShot(self):
        '''
        今動いていない弾を見つけ、インデックスを取得
        '''
        for shoti in range(len(self.shotList)):
            if shotList[shoti].isJudgeAlive() == False:
                return shoti
        # 全て動いている状態だと-1を返す
        return

    def init(self, x, y):
        '''
        空いている弾を探して初期化
        '''
        freei = self.searchFreeShot()
        if freei != -1:
            self.shotList[freei].init(x, y)

    def update(self, panelh):
        '''
        動作
        '''
        for shotSingle in self.shotList:
            shotSingle.update(shotmy, panelh)

    def draw(self):
        for shotSingle in self.shotList:
            shotSingle.draw()
