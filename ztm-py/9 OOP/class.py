# class
class Class_name:
    pass

# object
object_name = Class_name()

# instantiate means creating an object
# instances means objects

class Class_one:
    def __init__(self, name, age):       #constructor method it is autamatically call when we instantiate       #functions inside the class called as method
        self.nameone = name         #it is like the dictionary nameone is attribute and the property is the value of the variable name that you can access like class_obj_name.key_name
        self.ageone = age

    def run(self,new):
        print("run",new)

# creating object

obj_one = Class_one("hitesh",21)
print(obj_one.nameone, obj_one.ageone)
# op: hitesh 
obj_one.run("hi this is run function of obj_one")
# op: run

# creating object second of same class
obj_two = Class_one("hp",21)
obj_two.run("hi this is run function of obj_two")
# imp: here the class has methods like .run() and the class has also keys and value of its own like the nameone and ageone

# you can also attach some of your own values to the class
Class_one.attach = 10
print(Class_one.attach)

# class object attribute
class PlayerCharacter:
    a = 50          #this is called class object attribute
    def __init__(self, name, age):
        self.nameone = name
        self.ageone = age

    def run(self):                          #you have to pass self if you want to use the variable that you define in the __init__
        print(f"name = {self.nameone} , {PlayerCharacter.a}")     #you can also use this variables that you define in the __init__    
        # if you are using the __init__ variable you have to use self.variable_name and give the (self) inside the parameters of the function 
        # if you are using the class object attribute you have to use the class_name.variable_name

playerCharacter_one = PlayerCharacter("first name", 21)
playerCharacter_one.run()

# default parameters
class New_class:
    def __init__(self,name="default",age=21):    #this is the default parameters
        if (age > 18):
            self.student_name = name
            self.student_age = age
    
    def shout(self):
        print(f"name = {self.student_name}, age = {self.student_age}")

obj_of_new_class = New_class()
obj_of_new_class.shout()