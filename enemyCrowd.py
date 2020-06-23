import pyxel
from enemy import Enemy


ENEMY_CROWD_START_X = 0
ENEMY_CROWD_START_Y = 30
ENEMY_X_MAX = 5
ENEMY_Y_MAX = 3


class EnemyCrowd:

    def __init__(self):
        '''
        初期化
        '''
        self.mx = 2  # 敵一体のx方向移動量
        self.my = -5  # 敵一体のy方向移動量
        self.dir = 1  # 敵軍の移動向き
        self.singleSize = 16  # 敵一体のサイズ

        # 敵軍の配列初期化
        self.enemyList = [[Enemy((self.singleSize + 5)*i + ENEMY_CROWD_START_X, j * (self.singleSize + 5) +
                                 ENEMY_CROWD_START_Y, (i * ENEMY_Y_MAX + j) % 3) for i in range(ENEMY_X_MAX)] for j in range(ENEMY_Y_MAX)]

    def update(self, panelw, mt):
        '''
        移動
        panelw: 画面幅
        mt:移動タイミング/fps
        '''
        # タイミングが来たら移動を実行
        if pyxel.frame_count % mt == 0:

            # 壁についたときには上に上がると同時に移動方向を左右逆に変更
            if self.enemyList[0][0].x + self.mx * self.dir < 0 or \
                    self.enemyList[0][ENEMY_X_MAX-1].x + self.mx * self.dir + self.singleSize > panelw:
                for enemyi in range(ENEMY_Y_MAX):
                    for enemyj in range(ENEMY_X_MAX):
                        self.enemyList[enemyi][enemyj].update(0, self.my)
                self.dir *= -1  # 方向転換

            # そうでない場合には保持している向きに進む
            else:
                for enemyi in range(ENEMY_Y_MAX):
                    for enemyj in range(ENEMY_X_MAX):
                        self.enemyList[enemyi][enemyj].update(
                            self.mx * self.dir, 0)

    def draw(self):
        for enemyi in range(ENEMY_Y_MAX):
            for enemyj in range(ENEMY_X_MAX):
                self.enemyList[enemyi][enemyj].draw(self.singleSize)
