# there are many python modules that comes with the python installation

# like the random we seen before to create a random number , random is the module

# to use the module you have to first import that module 

import random

print(random)   #it will show you the location of the random module

# help(random)  #it will give you the info about the random

print(dir(random))  #it will show you all the methods that you can use with the random 

print(random.random())      #it will give the number between 0 to 1

print(random.randint(0, 13))

print(random.choice([1,2,43,5,56,6]))

mylist = [1,2,3,4,5,6]
random.shuffle(mylist)
print(mylist)