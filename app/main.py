'''search_from_googleのメインコード

ToDo
  - [ ] main.pyのリファクタリング
    - [ ] for文の2重ループをやめる
    - [ ] pythonのforは重いのでfor文自体をやめたい
'''

import os
import glob
import pandas as pd
import argparse
from dotenv import load_dotenv

from src.search import SearchFromGoogle
from src.util import make_output_file_path


load_dotenv()
OS_TYPE = os.getenv('OS_TYPE')
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')

# ファイルの入力先と出力先を変更する場合は以下の2つを変更
if OS_TYPE == 'WIN':
    INPUT_FILE_PATH = os.path.join('.', 'files', 'input')
    OUTPUT_FILE_PATH = os.path.join('.', 'files', 'output')
if OS_TYPE == 'MAC':
    INPUT_FILE_PATH = './files/input/'
    OUTPUT_FILE_PATH = './files/output/'

# 現状はcsvのみのサポートだが、追加する場合は以下にリストで追記する
SUPPORTED_EXTENTION = '*.csv'

# 入力するデータのカラム名を変更したい場合は以下を編集
INPUT_SEARCH_WORD = 'name'
# 出力するデータのカラム名を変更したい場合は以下を編集
OUTPUT_TITLE = 'title' # タイトル
OUTPUT_DETAIL = 'detail' # ディスクリプション
OUTPUT_URL_LINK = 'link' # リンク

# 実行時に取得する件数を入力して設定する
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', type=int, default=1)
args = parser.parse_args()


if __name__ == '__main__':
    files_path = glob.glob(os.path.join(INPUT_FILE_PATH, SUPPORTED_EXTENTION))

    # 高速化のためfor文はやめたい　案: files_pathをdfに保存して各ファイルpathにapplyかな〜
    for file_path in files_path:
        output_df = pd.DataFrame({
            INPUT_SEARCH_WORD: [],
            OUTPUT_TITLE: [],
            OUTPUT_DETAIL: [],
            OUTPUT_URL_LINK: []
        })
        output_path = make_output_file_path(INPUT_FILE_PATH, OUTPUT_FILE_PATH, file_path)
        df = pd.read_csv(file_path)

        for keyword in list(df[INPUT_SEARCH_WORD]):
            temp = SearchFromGoogle(CHROME_DRIVER_PATH, keyword).save_contents(args.length, INPUT_SEARCH_WORD ,OUTPUT_TITLE, OUTPUT_DETAIL, OUTPUT_URL_LINK)
            output_df = output_df.append(temp)

        output_df.to_csv(output_path, index=False)
