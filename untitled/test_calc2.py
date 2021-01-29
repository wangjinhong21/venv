
'''使用setup将公用的放在里面
使用@pytest.mark.parametrize将参数列表化
部分运行和全部运行
'''

import pytest

from calc import Calc


class TestCalc2:
    def setup(self):
        self.calc = Calc()

    # def teardown(self) -> None:
    #     print("____________________________________________________________")

    @pytest.mark.parametrize(["a", "b"], [(0, 0), (1, 3), (0.5, 0.7), (-1, 5)])
    def test_add(self,a,b):
        result=self.calc.add(a,b)
        print(result)

        # assert  4==result


    @pytest.mark.parametrize(["a", "b"], [(0, 0), (1, 3), (0.5, 0.7), (-1, 5)])
    def test_div(self,a,b):
        result = self.calc.div(a,b)
        print(result)

        # assert 3==result
    @pytest.mark.parametrize(["a", "b"], [(0, 0), (1, 3), (0.5, 0.7), (-1, 5)])
    def test_sub(self,a,b):
        result = self.calc.sub(a,b)
        print(result)



    @pytest.mark.parametrize(["a", "b"], [(0, 0), (1, 3), (0.5, 0.7), (-1, 5)])
    def test_mul(self,a,b):
        result = self.calc.mul(a,b)
        print(result)



    if __name__ =='__main__':
        pytest.main(['-vs'])
         #pytest.main(['-vs','test_calc2.py::TestCalc2::test_add'])  #执行一条
        # pytest.main(['-vs', 'test_calc2.py::TestCalc2::test_div'])  # 执行一条
        #  pytest.main(['-vs', 'test_calc2.py::TestCalc2::test_sub'])  # 执行一条
        #  pytest.main(['-vs','test_calc2.py::TestCalc2::test_mul'])  #执行一条

