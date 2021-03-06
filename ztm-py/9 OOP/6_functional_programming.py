# * pure function 
# * map()
# * filter()
# * zip()
# * reduce()
# lambda

# * pure function  
    #pure functions are these which does not interect with the outside world

# * map()
# map has the first parameter as a function and second parameter is ittrable

# normal method
def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    
    return new_list

print(multiply_by_2([1,2,3,4,5,6,7,8,9]))

# by map() method
def multiply_By_2(v):
    v *= 2
    return v

print(list(map(multiply_By_2, [1,2,3,4,5,6,7,8,9])))        #by the map() method you can create the list

# * filter()        # filter will filter the list and only keep the values that we want to keep
def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, [1,2,3,4,5,6,7,8,9])))         # if the condition is true it will accept the value otherwise it will ignore the value

# * zip()
my_list = [1,2,3,4,5,6,7,8,9]
my_list_2 = ["one","two","three","four","five","six","seven","eight","nine"]

print(list(zip(my_list, my_list_2)))
#you can also directly convert it into the dictionary
a = dict(zip(my_list, my_list_2))       
print(a)
# you can also zip more than two lists
my_list_3 = [1,2,3,4,5,6,7,8,9]
print(list(zip(my_list_2,my_list,my_list_3)))

# * reduce()
# for reduce we have to import the reduce from the funtools
from functools import reduce
mylist4 = [1,2,3,4,5,6,7,8,9]
def accumulator_function(acc, item):
    # print(acc, item)
    print(acc, item)
    return acc + item           #here the return will become the acc new value until the last ittrable  #and the last return will be the output

print(reduce(accumulator_function, mylist4, 5))      #here the 5 is an accumulator acc and item will be an ittrable that comes from the given mylist4       
                                                     #if you dont give the ittarable value it will automatic take the 0 value 


# lambda
# lambda expression in python are one time anonymous functions that you dont need more than ones
# lambda function have no name to it also we it will call automatically
print(list(map(lambda param: param * 2, [1,2,3,4])))        #here we dont have to declare the functions that we are going to use only once when we have the lambda