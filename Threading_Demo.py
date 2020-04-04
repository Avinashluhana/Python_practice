from threading import  *
from time import  sleep
class A(Thread):
    def run(self):
        for i in range(50):
            print("hi")
            sleep(2)
class B(Thread):
    def run(self):
        for x in range(50):
            print("Hello")
            sleep(2)

obj = A()
obj1 = B()

obj.start()
sleep(0.2)
obj1.start()
sleep(0.2)