# dunder method      dir
# __str__()
# __len__()
# __del__()
# __call__()
# __getitem__()



# dunder method      dir

# __str__()
class Toy():
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"the color is : {self.color}"

obj_Toy = Toy("red", 36)
print(str(obj_Toy))
# print(obj_Toy.__str__())



# __len__()
class Toy2():
    def __init__(self, color2, number2):
        self.color2 = color2
        self.number2 = number2

    def __len__(self):
        return 5

obj_Toy2 = Toy2("yello", 36)
print(len(obj_Toy2))
# print(obj_Toy2.__len__())


# __del__()                    #the delete keyword deleted some of variables from our programe
                            # useually it not in use beacause its bugy
class Toy3():
    def __init__(self, color3, number3):
        self.color3 = color3
        self.number3 = number3

    def __del__(self):
        print("deleted!")

obj_Toy3 = Toy3("yello", 36)
del obj_Toy3
# obj_Toy3.__del__()



# __call__()
class Toy4():
    def __init__(self, color4, number4):
        self.color4 = color4
        self.number4 = number4

    def __call__(self):
        print("this is the __call__ function inside the toy4")

obj_Toy4 = Toy4("yello", 36)
obj_Toy4()           #by call we can actually can call by using the object by just adding the () after the object name



# __getitem__()
class Toy5():
    def __init__(self, color5, number5):
        self.color5 = color5
        self.number5 = number5
        self.mu_dictionary = {
            "name" : "yoyo",
            "pets" : False
        }

    def __getitem__(self, i):
        return self.mu_dictionary[i]

obj_Toy5 = Toy5("yello", 36)
print(obj_Toy5["name"])