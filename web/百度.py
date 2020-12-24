from selenium import webdriver

class Testbaidu():
    def setup(self):
        self.driver=webdriver.chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        print("1111")