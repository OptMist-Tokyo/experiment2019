# ラズパイ実験第一回

## アイディア出し
https://docs.google.com/spreadsheets/d/1L0bNfCcR6HS0dS200it1oSSOJzrsGKEYGCI7eFDC8RA/edit?usp=sharing
- a チョークぶん投げるマシン[name=佐藤]
- c 計数民のツイートをゆっくりボイスで読み上げる[name=佐藤]
- a 授業実況（授業の状況をいろいろ認識してツイート）[name=佐藤]
- d 昼ゴハンで各食堂，店舗の混雑状況を報告[name=佐藤]
- c #定兼にアルゴリズムで勝つ,たかがアルゴリズムそう思っていませんか。それやったら明日もデータ構造が簡潔になりますよ[name=佐藤]
- d 控室の会話を英語に翻訳して読み上げることでTOEFL対策するぞ！[name=佐藤]
- d トイレの空き状況 [name=寺崎]
- a 教室の二酸化炭素濃度測るやつ [name=寺崎]
- a 顔認識で入出管理 [name=寺崎]
- a 時間割最適化 [name=寺崎]
- d 快適な目覚まし時計（起きないと寝顔がアップロードされる） [name=寺崎]
- d 学術的なGoogle Homeっぽいやつ（論文とか調べてくれる） [name=寺崎]
- d その日の気分に合わせてやる気の出る音楽を流してくれる [name=水谷]
- b 冷蔵庫内の食材の管理をしてくれる [name=水谷]
- b 足りてない栄養を検知する [name=水谷]
- c うそ発見器(会話してる人間の何かを認識してうそを発見するおもちゃ)　[name=水谷]
- c バズりそうなツイートを判定する　[name=水谷]
- 
- c 控室前に人が来たら勝手に学生証かざす装置 [name=金子]
- a 授業の教室の空席の数をLEDとかで表示 [name=金子]
- a 居眠りしたら音や光で起こす [name=金子]
- a 授業の終わりにチャイムを鳴らして授業時間を無視する先生を急かす [name=金子]
- b 適切な硬さになるまで生クリームを自動で混ぜる [name=金子]
- a 授業中に出てきた専門用語をググってwikiを表示 [name=金子]
- 
- d 花粉濃度(空気の汚れ)を検知[name=安部]
- d アルコール濃度を測る[name=安部]
- a 授業に関連したPDFを開く[name=安部]
- b 全自動ラズベリーパイ焼き器[name=安部]
- d 音漏れを検知して自動で音量を下げる[name=安部]


## まとめる
a. 授業サポート系
b. 食べ物
c. ネタ
d. QoL向上


## 備考
食堂の混雑状況，監視カメラ+ちょっとした画像認識ぐらいだったらできそう？

### 昼ごはんサポート系
各食堂のヒートマップ

### 控室サポート系
控室の空気の汚れ度合いを検知
空気清浄したい（換気を促す）
顔認識＋内側からドアノブを開ける（学生証かざす代わりに）
→外部の人間が来たらチョーク投げて撃退！！

### 授業サポート系
やめる気配がなかったらチャイム+チョーク

## 投票用まとめ案
1. 食堂の混雑状況→ヒートマップ化
[+α] 屋台村についてもヒートマップ化
2. 控室で顔認証→内側からドアノブを開ける
[+α] 外部生はチョークで撃退（卜部君もチョークで撃退）
3. 控室/教室の二酸化炭素濃度を検知→窓開けを促す
[+α] 空気清浄機，花粉情報も検知
4. 授業終わりにチャイム
[+α] それでも授業やめない教授にはチョークをお見舞い
5. <font color="red">#定兼にアルゴリズムで勝つ,たかがアルゴリズムそう思っていませんか。それやったら明日もデータ構造が簡潔になりますよ</font>

## 決定案
控室で顔認証→内側からドアノブを開ける
[+α] 外部生はチョークで撃退（卜部君もチョークで撃退）

技術的問題点
1. ドアノブをどうやって開ける？
2. 顔認証は簡単にできる？
3. ラズパイは結局焼く？→ <font color="ff1493">**絶対焼く！！**</font>

[サーボモータをPython+rapberry piで動かす](https://qiita.com/RyosukeKamei/items/9b15007bf1b77d33764f)


作り方参考：[甘酸っぱい✿ベリーベリーパイ✿ by Nancy town](https://cookpad.com/recipe/1250654)
見た目参考：[簡単☆可愛くておしゃれなベリーパイ♡ by ましゅこ](https://cookpad.com/recipe/5437362)


## 顔認証の解決策
[Amazon Rekognition 料金](https://aws.amazon.com/jp/rekognition/pricing/)

1ヶ月5000回呼び出しまで
1回の認証にデータベースに登録されている人数分のAPI呼び出し
→
前処理でありえない組合せは排除してAPI呼び出しを節約する

## ドア開ける解決策

## その他の追加のアイディア
顔認識じゃなくて音声で開けるのも良さそう（山？→川みたいな）

## 次回やること
- システムの名前決める
- ラズパイに慣れる
- ソフト部分書けるところはやっていく
- 必要な機材を検討
- 
- ラズベリージャムを作成（ラズベリー（ミックス）の購入）
- IHヒーターをもってくる
- 顔認証の動作確認，パイプライン作成

# ラズパイ実験第二回（4/26）

## 画像アップ用URL(お試し用)

http://mimari.php.xdomain.jp/login.html
(ユーザ名：raspie，パスワード：sakusaku)
## 本日の不真面目サイドの進捗
- 顔認証サイトをラズパイ上で動かす
→ひとまず作成完了。
→ファイル名に名前を含むように変更！
(DBとか使うといいかも) （DB勉強ヾ(●_ゝ-*)スルゾ!!）[name=金子]
- ジャムを作る( )→今からやります！サボっててすみませんでしたああああ！

## <font color="red">ラズパイ1段階目：ジャム</font>
- https://www.cuoca.com/articles/jam/
- ミックスベリー50g，グラニュー糖40g，レモン汁少々
- ベリー溶かしたときに出る水を利用
- 弱火で全体的にふつふつとなるまで煮る
- へらの跡がしっかり残る感じまで
![Imgur](https://i.imgur.com/BOizsQa.jpg)
- 冷やしたあと，かさがだいぶ減った
- かなりドロドロの状態に，色はブルーべリーの紫
- ブルーベリーは除いてトッピング用にするべき
- 【味】もう少し酸味がほしい→レモンで補う，砂糖60%
- 【食感】けっこう固めだが，パイに乗せるならアリ？
- カスタードとの取り合わせ→ココ重要!!

## カメラ使う
- ラズベリーpythonの練習。
- ラズベリーパイに繋げたカメラに映ってる画像を画面に映すやつをつくった。
- それにcを押すと画像を保存できる機能を追加した。

![Imgur](https://i.imgur.com/Yb8RSXl.jpg)
保存した画像
## GPIO使う
rpi.gpioをインストールした

![Imgur](https://i.imgur.com/dOFkY41.jpg)
やっている

## AWSの環境構築
AWS RekognitionをPythonのAPIを使って呼び出すためにboto3,awscliをインストールし，rekognitionのAPIを呼び出すテストを行なっているがなにか問題があるらしくエラーが返ってくる。→解決
画像をローカルのディレクトリから読み込み顔を検出するメソッドが正しく動作することを確認した。以下のコマンドを実行すると，
```
python3 ~/workspace/facerecognition/test_from_local.py
```
```
Detected labels in /var/www/html/files/sadakane.jpg
Head : 99.9814224243164
Hair : 96.28131103515625
Person : 95.76986694335938
Human : 95.76986694335938
Haircut : 87.98538208007812
Apparel : 78.93231964111328
Clothing : 78.93231964111328
Overcoat : 78.08843231201172
Suit : 78.08843231201172
Coat : 78.08843231201172
Attorney : 76.434814453125
Face : 75.42069244384766
Jaw : 71.3918228149414
Accessories : 71.13286590576172
Tie : 71.13286590576172
Accessory : 71.13286590576172
Black Hair : 60.92500305175781
Done...
```
のように出力され，物体検知ができていることがわかる。

## その他メモ
### raspberry piへのログイン方法
```
ssh pi@157.82.205.228
```
`157.82.205.228`はraspberry piのipアドレス(ist-membersに接続した状態でやること)．

### raspberry piにopencvをインスコ
```
pip3 install opencv-python 
sudo apt-get install libcblas-dev
sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
```
### IHヒーターの操作方法
1. 電源ボタンを押す
2. 加熱ボタンを押す
3. 火加減調整ボタンで調整する（ジャムは焦げやすいので弱めで（温度:１or2））
4. 煮詰まって来たら突沸を防ぐために保温モードに切り替える


## 必要な電子部品類
- サーボモータ
- スイッチ
    - http://akizukidenshi.com/catalog/g/gP-09826/
- LED
    - あるから必要無さそう？
- スピーカー
    - http://akizukidenshi.com/catalog/g/gP-05411/

## 顔認識システムの名前
- Face Pynition
- Recognipy
- pymission
- MEIPI ( Manager of Entering Interface by raspberry PI ) 

随時募集中！！

### 今日参考にしたリンク

- http://usicolog.nomaki.jp/engineering/raspberryPi/raspberryPi_Apache2.html
- https://webkaru.net/linux/scp-command/
- https://iotdiyclub.net/raspberry-pi-camera-python-1/
- http://www.ic.daito.ac.jp/~mizutani/raspi/blinkingLED.html
- https://note.nkmk.me/python-opencv-camera-to-still-image/
