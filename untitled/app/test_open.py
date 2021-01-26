
from appium import webdriver
desire_cap = {
  "platformName": "android",
  "appPackage": "com.chuangshen.jifan",
  "deviceName": "127.0.0.1:7555",
  "appActivity": ".java.ui.nav.HomeActivity"
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout")
el1.click()
