# 使い方説明
## 環境設定
必要なプログラム
```
python3.X
chromeDriver
```

### python 3.Xインストール
1. pythonがインストールされてない場合はpythonのダウンロードを行う
https://www.python.org/downloads/release/python-397/

*注意* : windowsの場合はインストールする際に　`Add Python 3.x to PATH` にチェックすること

### chromeDriverのインストール
1. 自分が現在使用しているchromeのバージョンを確認する
![alt text](./pic/chrome_ver.png)

2. 自分のchromeのバージョンに合わせたchromeDriverをダウンロードし、任意の場所へ保存する
https://chromedriver.chromium.org/downloads

3. `.env.sample` をもとにに保存したchromeDriverまでのパスを `CHROME_DRIVER_PATH=` に追加し、`.env` として保存する  
#### macの場合
```
CHROME_DRIVER_PATH={chromedriverまでのパス}/chromedriver
```

#### windowsの場合
```
CHROME_DRIVER_PATH={chromedriverまでのパス}/chromedriver.exe
```

### python環境に必要なものをインストール
#### macの場合
以下のコマンドを入力し、seach_from_googleフォルダ内にいることを確認
```
$ pwd
```

以下のコマンドを実行し、pythonに必要なパッケージをインストール
```
$ pip install -r requirements.txt
```

#### windowsの場合
以下のコマンドを実行し、seach_from_googleフォルダ内にいることを確認
```
> @cd
```

以下のコマンドを実行し、pythonに必要なパッケージをインストール
```
$ pip install -r requirements.txt
```

注意: 上記のコマンドがうまく動かない時は `pip3 install -r requirements.txt` を実行する


## 実行方法
1. `search_from_google` 内の　`files/input` 内にプログラムを実行したいファイルを配置する
2. windowsの場合は `@cd`  macの場合は `pwd` コマンドを実行し、カレントディレクトリが `search_from_google` であることを確認する
3. `python app/main.py` をコマンドで実行する
4. `seaech_from_google` 内の `files/output` 内にプログラムを実行した結果が配置される
