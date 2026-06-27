#Class methods
class emplo:
    company = "Google"
    def show(self):
        print(f"{self.name} works in {self.company}")

    
    # def change_comp(cls, newcompany):   #does not change the class variable(company) it just changes the instance variable
    #     cls.company = newcompany

    @classmethod
    def change_comp(cls, newcompany):   #does change class variable 'cause decorator has been used
         cls.company = newcompany

e1 = emplo()
e1.name = "Riva"
e1.show()
e1.change_comp("Microsoft")  #class variable remains 'Google' if '@classmethod' was not used
e1.show()
print(emplo.company)
              

#Class methods as alternative constructors
class emplo:
    def __init__(self, name, income):
        self.name = name
        self.income = income

    @classmethod    #for name-income like data
    def convert(cls, string):
        return cls(string.split('-')[0], int(string.split('-')[1]))
    
e1 = emplo('Riva', 80000)
print(e1.name)
print(e1.income)

e2 = emplo.convert('Riva-90000')
print(e2.name)
print(e2.income)