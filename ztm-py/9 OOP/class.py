# class
from os import name


class class_name:
    pass

# object
object_name = class_name()

# instantiate means creating an object
# instances means objects

class class_one:
    def __init__(self, name):       #constructor method it is autamatically call when we instantiate
        self.nameone = name         #it is like the dictionary nameone is key and the value is the value of the variable name that you can access like class_obj_name.key_name

    def run(self,new):
        print("run",new)

# creating object

obj_one = class_one("hitesh")
print(obj_one.nameone)
# op: hitesh 
obj_one.run("hi")
# op: run

# creating object second of same class
obj_two = class_one("hp")
obj_two.run("new")