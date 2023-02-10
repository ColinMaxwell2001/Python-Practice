import random

class Organism: # Eldest Parent Class
    def __init__(self, name):
        self.name = name
        print("an organism is created")

class Animal(Organism): # 1st Child Class
    info = " a living organism that feeds on organic matter\n"
    
    def __init__(self, name):
        super().__init__(name) 
        print("An animal is created")
        #self.name = name

class Dog(Animal): # 2nd Child Class
    info = "a domesticated and cuddly mammal that is awesome\n"
    
    def __init__(self, name):
        
        super().__init__(name) # runs constructor in Animal Class
        print("A Dog is created")
        self.lucky_number = random.randint(1,10)
        self.fur = ""
 
    
    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")


class Bulldog(Dog): # 3rd Child Class
    def __init__(self, name):
        super().__init__(name)
        print("A bulldog is created")

dog1 = Bulldog("Fido")

#dog1.bark()
print(dog1.info) # overrides info variable in Animal Class and uses Dog Class
      