# function  def
def new_function():
    print("function data")

new_function()      #we use this syntax to call/invoke a function

# positional parameters      #parameters are the variables that are provided to the function
def new_function2(name, rollno):                                #this are called as positional parameters
    print(f"hello {name} your roll no is {rollno}")

# argument        #arguments are the actvitual values
new_function2("hitesh", 21)

# keyword arguments
new_function2(rollno="twenty-one", name="tejas")

# default parameters
def new_function3(name = "hp", rollno = 21.21):
    print(f"hello {name} your roll no is {rollno}")

new_function3("hitesh")