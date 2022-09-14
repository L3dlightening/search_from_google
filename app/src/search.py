"""概要: google検索から検索結果を取得するためのモジュール"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class SearchFromGoogle:
    """google検索に関すること全般について記述されたクラス"""

    def __init__(self, driver_path, keyword):
        self.DRIVER = webdriver.Chrome(executable_path=driver_path)
        self.keyword = keyword

    def search_keyword(self):
        """google検索を行うためのドライバーを設定する"""
        url = "https://www.google.com/search?q={}&safe=off".format(self.keyword)
        time.sleep(1)
        self.DRIVER.get(url)

    def update_search_page(self, element_idx):
        """googleの検索ページを取得し、要素が見つからない場合は、ページの切り替えも行う"""

        try:
            h3_element = self.DRIVER.find_elements(
                    by=By.XPATH, value='//a/h3')[element_idx]
        except IndexError:

            element_idx = 0
            next_page = self.DRIVER.find_element_by_link_text('次へ')
            next_page.click()
            h3_element = self.DRIVER.find_elements(
                    by=By.XPATH, value='//a/h3')[element_idx]

        return h3_element, element_idx

    def search_cache(self, url):
        """google検索画面に戻りcacheを検索するモジュール"""
        self.DRIVER.get("https://www.google.com/")
        _search = "cache:" + url
        query = self.DRIVER.find_element(By.NAME, "q")
        query.send_keys(_search)
        query.send_keys(Keys.ENTER)
        time.sleep(1)

    def save_contents(self, length, COL_SEARCH_WORD, COL_TITLE, COL_DETAIL, COL_URL_LINK, COL_CACHE_LINK):
        """検索キーワードからタイトル、概要、リンクを取得する"""
        self.search_keyword()

        df_output = pd.DataFrame({
            COL_SEARCH_WORD: [],
            COL_TITLE: [],
            COL_DETAIL: [],
            COL_URL_LINK: []
        })

        for idx in range(length):
            if idx == 0:
                element_idx = 0

            try:
                h3_element, element_idx = self.update_search_page(element_idx)
            except NoSuchElementException:
                break

            df_output.loc[idx, COL_SEARCH_WORD] = self.keyword
            df_output.loc[idx, COL_TITLE] = h3_element.text
            df_output.loc[idx, COL_URL_LINK] = h3_element.find_element(
                    by=By.XPATH, value='..').get_attribute('href')

            try:
                df_output.loc[idx, COL_DETAIL] = self.DRIVER.find_elements(
                        by=By.CLASS_NAME, value="VwiC3b")[element_idx].text
            except IndexError:
                df_output.loc[idx, COL_DETAIL] = \
                        'エラーのため取得出来ませんでした。\
                        内容をご覧になりたい場合はURLから\
                        該当ページに飛んでください。'

            try:
                self.search_cache(df_output.loc[idx, COL_URL_LINK])
                df_output.loc[idx, COL_CACHE_LINK] = self.DRIVER.current_url
            except:
                df_output.loc[idx, COL_CACHE_LINK] = "キャッシュなし"
            element_idx += 1
        return df_output
