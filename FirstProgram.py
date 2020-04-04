class python_OOP:
	def fun(self,name):
            self.name=name
            return self.name


class inner_class:
        def fun(self,age):
            self.age=age
            return age


obj1 = inner_class()
print(obj1.fun(19))
obj = python_OOP()
print(obj.fun("avinash"))