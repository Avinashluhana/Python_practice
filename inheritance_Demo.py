class A:
    def fun():
        print("B")
        print("C")

obj = A()


class B(A):
    def fun1():
        print("D")
        print("F")

obj1 = B()
B.fun()
B.fun1()

