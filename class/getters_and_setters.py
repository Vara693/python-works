#Getters and Setters
class myclass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")

    #Getter
    @property
    def hen_value(self):
        return 100*self._value
    
    #Setter
    @hen_value.setter
    def hen_value(self, new):
        self._value = new/10
    
obj = myclass(11)
print(obj._value)
# obj._value = 78
# print(obj._value)
obj.hen_value = 120
obj.show()
print(obj.hen_value)