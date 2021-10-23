'''app/src/searchに関するテストを記述したファイル'''

import os
import pytest
from dotenv import load_dotenv

from app.src.search import SearchFromGoogle
from const import IDOL_TITLE, IDOL_DETAIL, IDOL_HREF, IDOL_TITLE2, IDOL_DETAIL2, IDOL_HREF2

load_dotenv()
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')


def test_検索ワードにアイドルマスターが入った時に特定の結果が返される():
    expected_title, expected_detail, expected_href = \
        SearchFromGoogle(CHROME_DRIVER_PATH, 'アイドルマスター').save_contents(1)

    assert expected_title[0] == IDOL_TITLE
    assert expected_detail[0] == IDOL_DETAIL
    assert expected_href[0] == IDOL_HREF


def test_検索ワードの取得件数を指定した時に件数分のリストが返ってくる():
    expected_title, expected_detail, expected_href = \
        SearchFromGoogle(CHROME_DRIVER_PATH, 'アイドルマスター').save_contents(2)

    assert expected_title[0] == IDOL_TITLE
    assert expected_detail[0] == IDOL_DETAIL
    assert expected_href[0] == IDOL_HREF
    
    assert expected_title[1] == IDOL_TITLE2
    assert expected_detail[1] == IDOL_DETAIL2
    assert expected_href[1] == IDOL_HREF2