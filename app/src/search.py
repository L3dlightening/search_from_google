'''概要: google検索から検索結果を取得するためのモジュール

Todo
  - [ ] SearchFromGoogleのクラス作成時にキーワードを__init__するのはイケてないのでリファクタリングしたい
  - [ ] 取得できる件数を可変できるようにsave_contentsを変更する
    - [ ] 関数の変更
    - [ ] テストの実装
'''

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchFromGoogle:
    '''google検索に関すること全般について記述されたクラス'''
    def __init__(self, driver_path, keyword):
        self.DRIVER = webdriver.Chrome(executable_path=driver_path)
        self.keyword = keyword


    def search_keyword(self):
        '''google検索を行うためのドライバーを設定する'''
        url = "https://www.google.com/search?q={}&safe=off".format(self.keyword)
        time.sleep(2)
        self.DRIVER.get(url)


    def save_contents(self, length):
        '''検索キーワードからタイトル、概要、リンクを取得する'''
        self.search_keyword()
        title_list = list(range(length))
        href_list = list(range(length))
        detail_list = list(range(length))

        for idx in range(length):
            h3_element = self.DRIVER.find_elements(by=By.XPATH, value='//a/h3')[idx]
            title_list[idx] = h3_element.text
            href_list[idx] = h3_element.find_element(by=By.XPATH, value='..').get_attribute('href')
            detail_list[idx] = self.DRIVER.find_elements(by=By.CLASS_NAME, value="VwiC3b")[idx].text

        return title_list, detail_list, href_list
