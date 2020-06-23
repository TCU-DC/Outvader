import pyxel
from enemy import Enemy

ENEMY_X_MAX = 3
ENEMY_Y_MAX = 5


class EnemyCrowd:

    def __init__(self):
        '''
        初期化
        '''
        self.mx = 10  # 敵一体のx方向移動量
        self.dir = 0  # 敵軍の移動向き
        self.my = -5  # 敵一体のy方向移動量
        self.singleSize = 16  # 敵一体のサイズ

        # 敵軍の配列初期化
        self.enemyList = Enemy[ENEMY_Y_MAX][ENEMY_X_MAX]
        for enemyi in range(len(enemyList)):
            for enemyj in range(len(enemyList[enemyi])):
                self.enemyList[enemyi][enemyj] = Enemy(
                    enemyi * (self.singleSize + 5), enemyj * (self.singleSize + 5), enemyi * ENEMY_Y_MAX + enemyj % 3)

    def update(self, panelw, panelh):

        # 壁についたときには上に上がると同時に移動方向を左右逆に変更
        if self.EnemyList[0][0] + self.mx * self.dir < 0 or \
                self.EnemyList[0][ENEMY_X_MAX] + self.mx * self.dir > panelw:
            for enemyi in range(len(enemyList)):
                for enemyj in range(len(enemyList[enemyi])):
                    self.enemyList[enemyi][enemyj].y -= self.my
            self.dir *= -1  # 方向転換

         # そうでない場合には保持している向きに進む
        else:
            for enemyi in range(len(enemyList)):
                for enemyj in range(len(enemyList[enemyi])):
                    self.enemyList[enemyi][enemyj].x += self.mx * self.dir

    def draw(self, kind):
        for enemyi in range(len(enemyList)):
            for enemyj in range(len(enemyList[enemyi])):
                self.enemyList[enemyi][enemyj].draw(self.singleSize)
