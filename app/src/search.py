import os
import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv

load_dotenv()
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')


class SearchFromGoogle:
    def __init__(self, keyword):
        self.DRIVER = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.keyword = keyword


    def search_keyword(self):
        url = "https://www.google.com/search?q={}&safe=off".format(self.keyword)
        time.sleep(2)
        self.DRIVER.get(url)


    def save_contents(self):
        self.search_keyword()

        elem_titles = self.DRIVER.find_elements_by_class_name("LC20lb")
        titles = []
        for titleElement in elem_titles:
            titles.append(titleElement.text)

        elem_details = self.DRIVER.find_elements_by_tag_name("a")
        details = []
        for detailElemet in elem_details:
            details.append(detailElemet.text)
        return titles, details

