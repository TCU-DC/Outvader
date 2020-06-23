import pyxel


class Player:

    def __init__(self, panelw, panelh):
        '''
        プレイヤーの初期化
        @param x&y 初期座標
        '''
        self.size = 16
        self.x = panelw / 2
        self.y = panelh - self.size - 5

    def update(self, panelw, panelh):
        '''
        移動を制御する
        '''
        # キーボード操作による移動
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.x += 1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.x -= 1

        # 壁で止まる
        # if self.x < 0:
        #     self.x = 0
        # elif self.x > panelw:
        #     self.x = panelw

    def draw(self):
        '''
        プレイヤーの描画を行う
        '''
        pyxel.blt(self.x, self.y, 1, 16*3, 0, 16, 16, 0)
        # pyxel.blt(0, 60, 1, 0, 0, 16, 16, 0)
