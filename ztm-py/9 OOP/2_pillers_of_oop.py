# 1 Encapsulation
# 2 Abstraction
# 3  Inheritance
    # isinstance
# 4 polymorphism


# there are 4 main pillers of OOP in every programming language

# 1 Encapsulation
    # encapsulation is the binding of data and functions that manupulates that data 
    # like in the class we encapsulate it into a one big object (class) that keepes everything into this box that users or code can interect with

# 2 Abstraction
    # abstration means hiding of information and giving actions to only whats necessary

# 3  Inheritance
    # inheritance allows new objects to take on the property of existing objects
    # to create the inherited class you just have to give the parent class name inside the brackets of child class

class User():               #it is the parent calss
    def sign_in(self):        
        print("hi this is the parent class")
    
class Wizard(User):         ##it is the child class
    def __init__(self, one, two):
        self.name = one
        self.power = two

    def attack(self):
        print(f"this is the Wizard class attack and \nthis is the first parameter : {self.name}, this is the second parameter : {self.power}")

class Archer(User):         ##it is the child class
    pass

obj1 = Wizard("abc","def")
obj2 = Archer()
obj1.sign_in()
obj2.sign_in()
obj1.attack()

# isinstance
print(isinstance(obj1, User))       #it used to check is the object is an instance of a pirticular class


# 4 polymorphism
    # poly means many and morphism means form that means many-form   #you still have to understand this by searching

# if you have same function name in the parent class and child class you can use by following
class User2():               #it is the parent calss
    def attack(self):
        print("this is the parent class attack method")
    
class Wizard2(User2):

    def attack(self):
        User2.attack(self)
        print("this is the Wizard class attack method")

wizard2_obj = Wizard2()
wizard2_obj.attack()