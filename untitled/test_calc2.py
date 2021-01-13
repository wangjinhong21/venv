import pytest

from calc import Calc


class TestCalc2:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize(["a", "b"], [(0, 0), (1, 3), (0.5, 0.7), (-1, 5)])
    def test_add_1(self,a,b):
        # self.calc=Calc()
        result=self.calc.add(a,b)
        print(result)
        # assert  4==result
    def test_div_1(self):
        # self.calc = Calc()
        result = self.calc.div(6, 2)
        print(result)
        # assert 3==result
    def test_div_2(self):
        # self.calc = Calc()
        result = self.calc.div(5, 0)
        print(result)


    if __name__ =='__main__':
        # pytest.main()
        pytest.main(['-vs','test_calc2.py::TestCalc2::test_add_1'])  #执行一条


