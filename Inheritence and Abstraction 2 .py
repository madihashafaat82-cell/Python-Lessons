#Parent class
class dad :
    def __init__(self , eyes , agressive ):
        self.eyes = eyes
        self.agressive = agressive

    def display(self):
        print("Your eye color is " , self.eyes)
        print("Your agressivness is " , self.agressive)
#Child class
class son(dad):
    def __init__(self, name , age , eyes, agressive):
        self.name = name
        self.age = age
        #invoking the __init__ of parent class
        #to accses the attributes
        super().__init__(eyes , agressive)

#Object creation
obj = son('Ahmed', 15 , 'Grey' , False)

#Calling Function
obj.display()