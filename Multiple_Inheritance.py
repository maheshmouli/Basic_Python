#Multiple Inheritance

class A:
    def method1(self):
        print("A class method is called")


class B(A):
    def method1(self):
        print('B class method is called')
    def method2(self):
        print('B class method2 is called')

class C(A):
    def method1(self):
        print('C method is called')

class D(B,C):
    def method1(self):
        print('D method is called')
        C.method1(self)
        B.method1(self)
        A.method1(self)

d = D()
print(d.method1())
