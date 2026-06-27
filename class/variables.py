# Class variables and Instance(object) variables
class company():
    noofemployee = 0  #class variables
    comp = "Microsoft"
    def __init__(self, name):
        self.name = name   #instance variables
        company.noofemployee += 1
    def info(self):
        print(f"\n{self.name} is an employee of {self.comp}.")
        print(f"Total employees are {self.noofemployee}")

emp1 = company('Radha')
emp1.info()
emp2 = company('Shivani')
# emp2.comp = "Google"
emp2.info()