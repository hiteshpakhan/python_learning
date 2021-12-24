# list
# .append()
# .insert()
# .extend()
# .pop()
# .remove()
# .clear()
# in
# .sort()
# sorted()
# reverse()
# .copy()
# .range()
# .join()


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
print(basket2.index(4))   #it will give the index of the number, that you provided inside the brackets
print(basket2.index(3, 1, 4))   #you can also give start and stope index for looking

print(1 in basket2)
print(10 in basket2)        #it willcheck if the first value is inside the second value

print(basket2.count(5))            #it will count the given value occourence inside the element 

#list method 3

basket3 = ["c","a","h","b","d","e","f","g"]
basket3.sort()
print(basket3)              #it will sort the list

newbasket3 = basket3.copy()
print(newbasket3)           #it will copy the data into another variable without assigning only address of the variable

basket3.reverse()
print(basket3)              #it will reverse the list

print(basket3[::-1])        #it also the type you can use to reverse the basket

# common list pattern

# range(start : stop)
print(list(range(1, 100)))  #it used to create the range
print(list(range(100)))

# .join()
sentence = " "
new_sentence = sentence.join(["hi","my","name","is","hitesh"])
print(new_sentence)


# list unpaking
a,b,c,*d = [1,2,3,4,5,6,7,8,9]