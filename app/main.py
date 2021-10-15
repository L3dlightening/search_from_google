import os
import glob
import pandas as pd

from src.search import SearchFromGoogle
from src.util import make_output_file_path


INPUT_FILE_PATH = './files/input/'
OUTPUT_FILE_PATH = './files/output/'

SUPPORTED_EXTENTION = '*.csv'

INPUT_SEARCH_WORD = 'name'
OUTPUT_TITLE = 'title'
OUTPUT_DETAIL = 'detail'
OUTPUT_URL_LINK = 'link'


if __name__ == '__main__':
    files_path = glob.glob(os.path.join(INPUT_FILE_PATH, SUPPORTED_EXTENTION))

    for file_path in files_path:
        output_path = make_output_file_path(INPUT_FILE_PATH, OUTPUT_FILE_PATH, file_path)
        df = pd.read_csv(file_path)
        for idx, row in df.iterrows():
            # ToDo ここに値をゲットするコードを追記
            df.loc[idx, OUTPUT_TITLE], df.loc[idx, OUTPUT_DETAIL], df.loc[idx, OUTPUT_URL_LINK] = \
                idx, idx, idx
            print(SearchFromGoogle(row[INPUT_SEARCH_WORD]).save_contents())
            df.to_csv(output_path, index=False)