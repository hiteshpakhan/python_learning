# higher order functions
# a higher order function can ether be function that accept another function 
def greet(func):
    func()

# or the higher order functions can be those that returns another function
def greet2():
    def func2():
        return "something"
    return func2

# means a higher ordered function can accept or return another function 

# example of higher order functions 
# map()
# filter()
# reduce()
# they are the HOF because they allaccept the function