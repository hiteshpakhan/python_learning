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