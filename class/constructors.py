#Constructors
class flavour:
    def __init__(self):
        print("Some of the flavours you are looking for.")
ul = flavour()

class people:
    def __init__(self, name, occ):
        print("Welcome to our company!")
        self.name = name
        self.occ = occ
    def info(self):
        print(f'{self.name} is a {self.occ}')

a = people('Varad', 'CEO')
b = people('Riva', "Manager")
a.info()
b.info()