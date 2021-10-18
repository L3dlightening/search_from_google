'''app/src/searchに関するテストを記述したファイル'''

import os
import pytest
from dotenv import load_dotenv

from app.src.search import SearchFromGoogle
from const import IDOL_TITLE, IDOL_DETAIL, IDOL_HREF

load_dotenv()
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')


def test_検索ワードにアイドルマスターが入った時に特定の結果が返される():
    expected_title, expected_detail, expected_href = \
        SearchFromGoogle(CHROME_DRIVER_PATH, 'アイドルマスター').save_contents()
    assert expected_title == IDOL_TITLE
    assert expected_detail == IDOL_DETAIL
    assert expected_href == IDOL_HREF
