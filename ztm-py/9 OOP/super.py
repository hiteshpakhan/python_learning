# we know that we can inherite the child from the parent class 
# but we dont know that how to give __init__ in the parent class
# so if we use the __init__ in the parent class we have to use the super to give the values


class User():
    def __init__(self, three):
        self.thirdvalue = three

    def sign_in(self):
        print("hi this is the parent class : ", self.thirdvalue)
    
class Wizard(User):
    def __init__(self, one, two, three):
        super().__init__(three)         #it is the super it will pass the value to the parent __init__
        self.name = one
        self.power = two

    def attack(self):
        print(f"this is the Wizard class attack and \nthis is the first parameter : {self.name}, \nthis is the second parameter : {self.power}, \nthis is the value of super : {self.thirdvalue}")

obj1 = Wizard("first value of Wizard", "second value of wizard", "third value of super")
obj1.attack()
obj1.sign_in()