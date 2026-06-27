#Classes and OOP
class person:
    name = 'Varad'
    occupation = 'Developer'
    age = 19
    income = 150000
    def info(self):
        print(f"{self.name} has a monthly income of ₹{self.income}")
a = person()
a.info()
b = person()
b.name = 'Riva'
print(b.name)

class rectangle:
    a = 10
    b = 7
    def area(self):
        print("Area: ", self.a*self.b)
    def pera(self):
        print("Perameter: ", 2*(self.a+self.b))
a = rectangle()
a.area()
a.pera()
b = rectangle()
b.a = 50
b.b = 9
b.area()