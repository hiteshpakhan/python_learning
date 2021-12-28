# dunder method         dir

# __str__()
class Toy():
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"the color is : {self.color}"

obj_Toy = Toy("red", 36)
print(str(obj_Toy))
print(obj_Toy.__str__())