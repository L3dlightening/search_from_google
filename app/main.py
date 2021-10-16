import os
import glob
import pandas as pd

from src.search import SearchFromGoogle
from src.util import make_output_file_path
from dotenv import load_dotenv

load_dotenv()
OS_TYPE = os.getenv('OS_TYPE')

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


if __name__ == '__main__':
    files_path = glob.glob(os.path.join(INPUT_FILE_PATH, SUPPORTED_EXTENTION))

    for file_path in files_path:
        output_path = make_output_file_path(INPUT_FILE_PATH, OUTPUT_FILE_PATH, file_path)
        df = pd.read_csv(file_path)
        for idx, row in df.iterrows():
            df.loc[idx, OUTPUT_TITLE], df.loc[idx, OUTPUT_DETAIL], df.loc[idx, OUTPUT_URL_LINK] = \
                SearchFromGoogle(row[INPUT_SEARCH_WORD]).save_contents()

        # df[[OUTPUT_TITLE, OUTPUT_DETAIL,OUTPUT_URL_LINK]] = \
        #     df.apply(SearchFromGoogle().save_contents(), result_type='expand')

        df.to_csv(output_path, index=False, encoding="shift-jis")
