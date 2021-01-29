
from selenium import webdriver
from time import sleep


class Test_Openbaidu():
    def setup(self):
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        # self.driver.find_element_by_link_

