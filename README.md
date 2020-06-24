
# システム概要
<img src="https://user-images.githubusercontent.com/46548311/85531564-d9226800-b649-11ea-9f23-c93de56bf120.PNG"><br>
pythonのライブラリであるpyxelを用いて作成したシューティングミニゲーム。  

# 使用言語/ライブラリ

## :speech_balloon:言語
- 【python3.7.4】/[document](https://www.python.org/)
<img src="https://cdn.svgporn.com/logos/python.svg" width="60px"><br>

## :closed_book:ライブラリ
- 【 pyxel 】/ [document](https://github.com/kitao/pyxel/blob/master/README.ja.md) <br>
<img src="https://raw.githubusercontent.com/kitao/pyxel/master/images/pyxel_logo_152x64.png" width="120px"><br>

# 環境構築について

## <img src="https://cdn.svgporn.com/logos/python.svg" width="30px">pythonの環境構築

**[ダウンロードサイト](https://www.python.org/downloads/)**

### :mountain_cableway:Windows向け 
[参考サイト](https://prog-8.com/docs/python-env-win)

### :apple:Mac向け
[参考サイト](https://prog-8.com/docs/python-env)
(ぶっちゃけよくわからない...)

### :penguin:Linux向け
[参考サイト](https://web-camp.io/magazine/archives/13267)
(こっちもよくわからない...)

## <img src="https://raw.githubusercontent.com/kitao/pyxel/master/images/pyxel_logo_152x64.png" width="60px">pyxelの導入について

**★python3.6.8以上であること**

### :mountain_cableway:Windows
```
pip install -U pyxel
```

### :apple:Mac

```
pip3 install -U pyxel
```

### :penguin:Linux

**Ubuntsu**

```
sudo apt install python3 python3-pip libsdl2-dev libsdl2-image-dev gifsicle
sudo -H pip3 install -U pyxel
```

**その他の環境**

以下を準備
- C++のビルド環境 (gcc、makeコマンドを含む)
- libsdl2-dev、libsdl2-image-dev
- Python3 (バージョン3.6.8以上)、pipコマンド

任意のフォルダで以下のコマンドを実行する
```
git clone https://github.com/kitao/pyxel.git
cd pyxel
make -C pyxel/core clean all
pip3 install .
```

[詳しくは公式チュートリアルを参考](https://github.com/kitao/pyxel/blob/master/README.ja.md)
