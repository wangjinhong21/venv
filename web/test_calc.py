# import sys
#
# print(sys.path)  #打印出查找代码的路径
# sys.path.append('..')#添加上一级路径

import unittest
# import pytest

# from python.calc import calc ##11
import Calc as Calc


class TestCal(unittest.TestCase):
    print("22")
    def test_add_1(self):
        self.calc=Calc()
        result= self.calc.add(1,2)
        self.assertEqual(3,result)
        print(result)
        print("1111111")

# class TestCal(unittest.TestCase):
#     print("22")
#     def test_add_1(self):
#         print("111111111122")

if __name__=='__main__':#python的入口函数
     pytest.main()
