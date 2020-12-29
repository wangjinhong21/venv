
# from python.calc import Calc
import calc
import pytest

class TestCalc:
    def setup(self):
        self.calc1 =calc()

    def test_add_1(self):
       # self.calc = calc()
        result = self.calc1.add(1 ,2)
        print(result)
        assert 3 == result

    def test_div(self):
        #self.calc = calc()
        result =self.calc1.div(2,2)
        assert 1== result

if __name__=='__main':
    pytest.mian(['-vs','test_pytest.py::TestCalc::test_div'])