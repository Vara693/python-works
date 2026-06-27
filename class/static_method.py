#static method
class Math():
    def __init__(self,num):
        self.num = num
    def add_num(self,n):
        self.num += n

    @staticmethod  #used when you know this can be accessable without class
    def add(a,b):  #but still want the class user to access it. 
        return (a+b)

a = Math(5)
print(a.num)
a.add_num(56)
print(a.num)
print(a.add(5,6))
print(Math.add(3,67))