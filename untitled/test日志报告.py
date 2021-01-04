import unittest


class TestTest(unittest.TestCase):
    """测试HTMLTestRunner"""
    def setUp(self):
        self.a=1
        self.b=2
        self.c=[1,2,3]

    def test_a_plus_b(self):
        """a+b=3 这个测试用例应该通过"""
        print('a+b=3')
        self.assertEqual(self.a+self.b,3)

    def test_a_minus_b(self):
        """a-b=3,这个用例应失败"""
        print('a-b=3')
        self.assertEqual(self.a-self.b,3)

    def test_a_multi_b(self):
        """a*b=2,这个用例应该成功"""
        print('a*b=2')
        self.assertEqual(self.a*self.b,2)

    def test_a_divide_c(self):
        """a/c=1这是个有SubTest的用例"""
        for i in self.c:
            with self.subTest(i=1):
                print('a/c=1')
                self.assertEqual(slef.a/i,1)

    def test_a_error_case(self):
        """除零正常"""
        print('1/0')
        self.assertEqual(self.a/0,1)

class ExampleCase2(unittest.TestCase):
    def setUp(self):
        self.a=4
        self.b=3

    def test_divide(self):
        print('我要打印输出')
        self.assertEqual(self.a / self.b, 2)


class ExampleCase2(unittest.TestCase):

    def test_plus(self):
        """用例3，plus，此用例执行出错，因为c未定义"""
        self.assertEqual(self.a*self.b,c)



class ExampleCase3(unittest.TestCase):
    """此class包含一个用例：divide-ok"""
    def setUp(self):
        self.a,self.b =4,2

    def test_divide(self):
        print('我要打印输出')
        self.assertEqual(self.a/self.b,2)

if __name__=='__main__':
    report_title='Example用例执行报告'
    desc='用于展示修改样式后的HTMLTestRunner'
    report_file='./ExampleReport.html'

    testsuite=unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTest))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase1))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase2))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase3))

    with open(report_file,'wb')as report:
        HTMLTestRunner_PY3(stream=report,title=report_title,description=desc)
        runner.run(testsuite)