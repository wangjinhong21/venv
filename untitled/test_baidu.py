from time import sleep, time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_baidu():
    def setup(self):
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("奥黛丽赫本")
        sleep(3)
        self.driver.find_element(By.ID,'su').click()
        sleep(3)

