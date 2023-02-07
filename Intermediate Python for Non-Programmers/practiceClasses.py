class Dog:
    # Class Attribute (variable)
    info = "a domesticate animal that is sometimes cute and cuddly"
    
    # No-args Constructor
    def __init__(self): #self is basically java equivalent of "this."
        print("\nI am in the Constructor!\n")
    
    # Overloaded Constructor
    def __init__(self, name):
        self.name = name
        print("Currently in overloaded Constructor with " , self.name , "!\n")
        
    # Method
    def barking(self):
        print("\nI am a dog and I am barking\n")
    

#Regular Method within no class
def getUserInput():
    # Retrieving Input from a User
    val = input("Enter your name: ")
    return val


# Main Method()
def main():
    #d = Dog() #Instance of Dog / Calls the init function (constructor)
    
    # name = getUserInput return
    name = getUserInput()
    
    d2 = Dog(name)
    print(d2.info)   # Printing info variable 
    d2.barking()     # Calling Barking method 



# Required in Every Program in order for program to recognize the main method()
if __name__ == "__main__":
    main()