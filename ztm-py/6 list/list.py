# list is a data type which is collection of objects that can be of any type
# in other programming languages you might heard the word arrays , list is just like that

li = [1, "cAT", True, "dog"]
print(li)           # op---     [1, 'cAT', True, 'dog']
print(li[2])        # op---     True

# List Slicing
amazon_cart = [
    "notebook",
    "sunglasses",
    "toys",
    "graps"
]

# list_name[start:stop:stepover]

# unlike the strings you can here change the data inside the list by assigning the new values
amazon_cart[0] = "new value" 
print(amazon_cart)


# matrix : matrix is just like the list of lists
matrixone = [
    [1,2,3],
    [4,5,6],
    [5,7,3]
]
print(matrixone[0][2])
print(len(matrixone))


# methods with list
basket = [1,2,3,4,5]
basket.append(100)
print(basket)

basket.insert(3, 100)
print(basket)

basket.extend([3, 1, 5])
print(basket)

basket.pop()
print(basket)             #it will remove the last element from the list

basket.pop(6)
print(basket)             #it will remove the data from the list at the index you provied to it

basket.remove(4)
print(basket)             #it will remove the number from the list

basket.clear()
print(basket)             #it will empty the list


# list methods 2

basket2 = [1,2,3,4,5,6]
print(basket2.index(4))   #it will give the index of the number you provide inside the brackets
print(basket2.index(3, 1, 4))   #you can also give start and stope index for looking