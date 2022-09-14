"""search_from_googleのメインコード"""

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
COL_SEARCH_WORD = 'name'
# 出力するデータのカラム名を変更したい場合は以下を編集

COL_TITLE = 'title'
COL_DETAIL = 'detail'
COL_URL_LINK = 'link'
COL_CACHE_LINK = 'cache'

# 実行時に取得する件数を入力して設定する
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', type=int, default=1)
args = parser.parse_args()


if __name__ == '__main__':
    files_path = glob.glob(os.path.join(INPUT_FILE_PATH, SUPPORTED_EXTENTION))

    for file_path in files_path:

        df_output = pd.DataFrame({
            COL_SEARCH_WORD: [],
            COL_TITLE: [],
            COL_DETAIL: [],
            COL_URL_LINK: []
        })

        output_path = make_output_file_path(
                INPUT_FILE_PATH, OUTPUT_FILE_PATH, file_path)
        df_keyword = pd.read_csv(file_path)
        keywords = list(df_keyword[COL_SEARCH_WORD])

        for keyword in keywords:
            df_single_keyword_search_results = SearchFromGoogle(
                    CHROME_DRIVER_PATH,
                    keyword
                ).save_contents(
                    args.length,
                    COL_SEARCH_WORD,
                    COL_TITLE,
                    COL_DETAIL,
                    COL_URL_LINK,
                    COL_CACHE_LINK)

            df_output = pd.concat(
                [df_output, df_single_keyword_search_results],
                ignore_index=True
            )

        df_output.to_csv(output_path, index=False)
