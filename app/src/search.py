'''概要: google検索から検索結果を取得するためのモジュール'''

import os
import time
import pandas as pd
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


    def save_contents(self, length, INPUT_SEARCH_WORD ,OUTPUT_TITLE, OUTPUT_DETAIL, OUTPUT_URL_LINK):
        '''検索キーワードからタイトル、概要、リンクを取得する'''
        self.search_keyword()

        output_df = pd.DataFrame({
            INPUT_SEARCH_WORD: [],
            OUTPUT_TITLE: [],
            OUTPUT_DETAIL: [],
            OUTPUT_URL_LINK: []
        })

        for idx in range(length):
            h3_element = self.DRIVER.find_elements(by=By.XPATH, value='//a/h3')[idx]
            output_df.loc[idx, INPUT_SEARCH_WORD] = self.keyword
            output_df.loc[idx, OUTPUT_TITLE] = h3_element.text
            output_df.loc[idx, OUTPUT_URL_LINK] = h3_element.find_element(by=By.XPATH, value='..').get_attribute('href')
            output_df.loc[idx, OUTPUT_DETAIL] = self.DRIVER.find_elements(by=By.CLASS_NAME, value="VwiC3b")[idx].text

        return output_df
