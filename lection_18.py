class A:
    def __init__(self):
        print("Class A")
        super().__init__()

class B(A):
    def __init__(self):
        print("Class B")
        super().__init__()
        # A.__init__()

class X:
    def __init__(self):
        print("Class X")
        super().__init__()

class Forward(B, X):
    def __init__(self):
        print("Class Fprward")
        super().__init__()

class Becward(X, B):
    def __init__(self):
        print("Class Becward")
        super().__init__()

b = B()
x = X()
f = Forward()
bb = Becward()

class Cls_1:
    def m(self):
        print("m from Cls_1")

class Cls_2(Cls_1):
    def m(self):
        print("m from Cls_2")
        super().m()

class Cls_3(Cls_1):
    def m(self):
        print("m from Cls_3")
        super().m()

cls_1 = Cls_1()
cls_2 = Cls_2()
cls_3 = Cls_3()

cls_1.m()
cls_2.m()
cls_3.m()

class Cls_4(Cls_2, Cls_1):
    pass 

cls_4 = Cls_4()
cls_4.m()

# class Cls_5(Cls_1, Cls_2):
#     pass 

# cls_5 = Cls_5()
# cls_5.m()
# cls_5.a_cls_1()

class Cls_6(Cls_2, Cls_1):
    def m(self):
        print("m from Cls_6")

cls_6 = Cls_6()
cls_6.m()

class Cls_7(Cls_2, Cls_3):
    def m(self):
        print("m from Cls_7")

cls_7 = Cls_7()
cls_7.m()
cls_3.m()
cls_2.m()
cls_1.m()

class Cls_8(Cls_2, Cls_3):
    def m(self):
        print("m from Cls_8")
        Cls_2.m(self)
        Cls_3.m(self)
        Cls_1.m(self)

cls_8 = Cls_8()
cls_8.m()

class Cls_9(Cls_2, Cls_3):
    def m(self):
        print("m from Cls_9")
        super().m()

cls_9 = Cls_9()
cls_9.m()

class TestCls:
    test_var = "Thos is a class variable"

    def __init__(self):
        self.test_var = "this is an instance variable"

print(TestCls.test_var)
TestCls.test_var = "new value"
print(TestCls.test_var)

t1 = TestCls()
print(t1.test_var)
t2 = TestCls()
t1.test_var = "new value 1"
print(t1.test_var)
print(t2.test_var)

class TestCls1:
    test_var = "this is a class variable"

t11 = TestCls1()
print(t11.test_var)

t11.test_var = 111
print(t11.test_var)
print(TestCls1.test_var)
