import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test_weixin():

    def setup_method(self,method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options) #查找cookie
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(5)

    def teardown_method(self, method ):
        self.driver.quit()

    def test_weixin(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        #
        db = shelve.open("cookies")
        # db['cookie']=self.driver.get_cookies()
        cookies =db['cookie']
        #
        for cookie in  cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # db['cookie']=self.driver.get_cookies()
        # # print(self.driver.get_cookies())
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(5)
        db.close()



