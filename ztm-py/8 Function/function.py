# function  def
# positional parameters
# argument
# keyword arguments
# default parameters
# return
# Docstring  help() & __doc__
# *args
# **kwargs

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

# return
def sum(num1, num2):
    return num1 + num2

print(sum(5,6))

# Docstring  help() & __doc__
def test():
    '''
    this is some info about this function
    '''
    print("hi there")

help(test)          #by using help you can find the info that written by the creator of the function
#there another method to do that
print(test.__doc__)

# *args
def func1(*hoo):
    print(hoo)

func1(1,2,3,4,5)

# **kwargs         #learne it next time to much for today