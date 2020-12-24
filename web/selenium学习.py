#import selenium
from selenium import webdriver


def test_selenium():
    print("1111111")
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
  #  print(a)
test_selenium()