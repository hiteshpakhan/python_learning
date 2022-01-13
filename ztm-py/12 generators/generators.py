# generators
    # generators are allow us to generate a sequence of values over time
    # for example : range()
# imp    # generators allow us to use a special type of symboal that called as yield that can pause and resume the functions
    
# yield : yield pauses the function and comes back to it when we do next to it



# when we use something like list ittrating it create a gient list at once responsible for using big amount of memory
# but on the other hand the yield ittrating happens one by one and not use the big amount of memory data

# so the use of yield is really benificial working with


# creating a generator
def gen1(num):
    for i in range(num):
        yield i
        print("this is the after yield ",i)

for item in gen1(5):
    print(item)




# range by the generators

class MyGen():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):         # __iter__ just like the iter() function  
        return self

    # def __next__(self):
    #     if

gen = MyGen(0, 100)
for i in gen:
    print(i)