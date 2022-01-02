# it is the python random module you can search this on the "askpython" website
import random

# random_int = random.randint(1,20)
list1 = []
i = 0
while i < 5:
    list1.append(random.randint(1,100))
    i += 1

print(list1)