'''概要: google検索から検索結果を取得するためのモジュール'''

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from dotenv import load_dotenv

load_dotenv()
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')


class SearchFromGoogle:
    '''google検索に関すること全般について記述されたクラス'''
    def __init__(self, keyword):
        self.DRIVER = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.keyword = keyword


    def search_keyword(self):
        '''google検索を行うためのドライバーを設定する'''
        url = "https://www.google.com/search?q={}&safe=off".format(self.keyword)
        time.sleep(2)
        self.DRIVER.get(url)


    def save_contents(self):
        '''検索キーワードからタイトル、概要、リンクを取得する'''
        self.search_keyword()

        h3_element = self.DRIVER.find_element(by=By.XPATH, value='//a/h3')
        title = h3_element.text
        href = h3_element.find_element(by=By.XPATH, value='..').get_attribute('href')
        detail = self.DRIVER.find_element(by=By.CLASS_NAME, value="VwiC3b").text

        return title, detail, href
