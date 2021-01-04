import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupClass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown Class")
    def setUp(self) -> None:
        print("setup")
    def tearDown(self) -> None:
        print("teardowm")
    def test_case01(self):
        print("testcase01")
        self.assertEqual(2,2,"判断相等")
    def test_case02(self):
        print("testcase02")
        self.assertEqual(2,2,"判断相等")
    @unittest.skipIf(1+1==2,"跳过下面这条用例")
    def test_demo_case03(self):
        print("testcase03")
        self.assertEqual(2,2,"判断相等")

class demo1(unittest.TestCase):
        def test_demo1_case0(self):
            print("test_demo1_demo0")
        def test_demo1_case1(self):
            print("test_demo1_demo1")


class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print("test_demo2_demo0")

    def test_demo2_case1(self):
        print("test_demo2_demo1")

if __name__ == '__main__':
        # unittest.main()
        # suite =unittest.TestSuite()
        # suite.addTest(demo("test_case01"))
        # suite.addTest(demo1("test_demo1_case0"))
        # unittest.TextTestRunner().run(suite)

        # suite = unittest.TestLoader().loadTestsFromTestCase(demo)
        # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
        # suiteall = unittest.TestSuite([suite,suite1])
        # unittest.TextTestRunner().run(suiteall)

        discover=unittest.defaultTestLoader.discover("./",'test*.py') #当前路劲下，匹配test开头的py文件
        unittest.TextTestRunner().run(discover)

