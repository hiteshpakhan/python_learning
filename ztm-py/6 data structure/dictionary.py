# dictionary {dict} {}
# .get()
# .get(finding key, or default value)
# dict()
# in
# .keys()
# .values()
# .items()
# .copy()
# .clear()
# .pop()
# .popitem()
# .update()



# dictionary {dict}
# dictonary is a collection of key and value it is just like the object in the javascript and it stores the data inside the querly brackets
# imp :- dictionary is not unordered it is not like the list that remember the line in which they inserted if the dictionary is very big we will not abele to access the indexing properly

dictonary_one = {
    "key1" : 1,
    "key2" : "two",
    "key3" : [1,2,3],
    "key4" : True
}
print(dictonary_one)
print(dictonary_one["key3"])
print(dictonary_one["key3"][2])


# dictionary method

# .get()
print(dictonary_one.get("key5"))        #it will check if the value is present in the dictonary if it is then it will give the value or it will give "none"

# .get(finding key, or default value)
print(dictonary_one.get("key5", 35))    #now when the value not present it will give the default that we already give to it

# dict()    it used to create the dictonary also

# in
print("key1" in dictonary_one)              #it willcheck in all the dictonary if the value is present

# .keys()
print("key1" in dictonary_one.keys())       #it will check if the value present in keys of the dictonary

# .values()
print("key1" in dictonary_one.values())     #it will check if the value present in the value in the dictonary

# .items()
print(dictonary_one.items())

# .copy()
dictonary_two = dictonary_one.copy()
print(dictonary_two)                        #it will copy the dictonary_one data into the dictonary_two 

# .clear()
dictonary_one.clear()
print(dictonary_one)        #it will delete all the keys and values from the dictonary

# .pop()
print(dictonary_two.pop("key2"))            #it will remove the key & value of the key you give
print(dictonary_two)

# .popitem()
print(dictonary_two.popitem())              #it will randomely pop any item from the dictionary
print(dictonary_two)

# .update()
print(dictonary_two.update({"key1" : 11}))  #it is used to update the value of the key