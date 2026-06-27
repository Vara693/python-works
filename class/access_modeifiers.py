#Access Modifiers (Python dont have its own access modifiers, the following are just built by programmers like us.)
#1.public access modifiers
class emplo:
    def __init__(self):
        self.name = 'Varadraj'
obj = emplo()
print(obj.name)

#2.private access modifiers
class emplo:
    def __init__(self):
        self.__name = 'Varadraj'
obj = emplo()
# print(obj.name) #doesn't generate the output 
print(obj._emplo__name) #mangling in python(indirrect access)
print(dir(obj))

#3.protected access modifiers
class emplo:
    def __init__(self):
        self._name = 'Varadraj'
obj = emplo()
print(obj._name)