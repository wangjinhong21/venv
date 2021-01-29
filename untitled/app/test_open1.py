import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Test_open1():
    def setup(self):
        desire_caps= {}
        desire_caps['platformName']= 'android'
        desire_caps['appPackage']= 'com.chuangshen.jifan'
        desire_caps['deviceName']= '127.0.0.1:7555'
        desire_caps['appActivity']= '.java.ui.nav.HomeActivity'
        desire_caps['noReset']= 'True'   #启动app时不要清除app里的原有的数据

        self.driver= webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_caps)

        self.driver.implicitly_wait(10)     #  隐式等待，每一次都会等待，全局的，默认0.5s一次

    def teardown(self):
        self.driver.back()
        self.driver.quit()


    def test_open1(self):
        self.driver.find_element_by_id("com.chuangshen.jifan:id/tv_home_search_").click()
        self.driver.find_element_by_id("com.chuangshen.jifan:id/editText").send_keys("衣服")
        self.driver.find_element_by_id("com.chuangshen.jifan:id/rb_tb").click()
        time.sleep(5)
    # def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("销量")').click()
        time.sleep(5)
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().'
        #                                                 'textContains("花花公子羽绒服男2020冬季新款帅气休闲外套男潮百搭加厚上衣冬装").instance(0));').click()
        #
        # time.sleep(5)

    #def test_touchaction(self):
        action=TouchAction(self.driver)
        window_rect=self.driver.get_window_rect()
        width=window_rect['width']
        height=window_rect['height']
        x1=int(width/2)
        y_start=int(height*4/5)
        y_end =int(height*1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()




if __name__ =='__main__':
    pytest.main()

