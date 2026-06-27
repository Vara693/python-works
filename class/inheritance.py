class emplo:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def show(self):
        print(f'The employee with {self.id} is {self.name}')

#Inheritance of class emplo
class mana(emplo):
    def pro(self):
        print('The most common is paranoid of pros')

e1 = emplo('Rohit', 5678)
e1.show()
e2 = mana('Mohit', 5687)
e2.show()
e2.pro()