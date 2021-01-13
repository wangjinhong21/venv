class Calc:

    def add(self,a:int,b:int):
        return a+b

    def div(self,a,b):
        if b==0:
            print("除数不能为0")
        else:
         return a/b

    def mul(self,a,b):
        return a*b

    def sub(self,a,b):
        return a-b