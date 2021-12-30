# decorators have the @ sign at the starting and name next to it 
# @classmethod and @staticmethod are the two decorators that we seen before
# decorators supercharge our functions

# decorators is a simply  a function that raps another function and enhances it or changes it

def my_decorator(func):
    def wrap_func():
        print("*****")
        func()                  #here the func() will be hello()
        print("######")
    return wrap_func

@my_decorator
def hello():
    print("hello")

hello()               #it will take the hello as a argument of a my_decorators 

# also we can use as many as we wnt
@my_decorator
def say():
    print("shout")

say()


# but if we have to passing the argument into the decorator function as well then first we have to assign the arguments into the main function as well

def demo(param):
    def fun(x):
        print("*****")
        param(x)
        print("######")
    return fun

@demo
def fun2(a):
    print(a)

fun2("with function")