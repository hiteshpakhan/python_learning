# dictionary {dict}
# dictonary is a collection of key and value it is just like the object in the javascript and it stores the data inside the querly brackets

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
print("key1" in dictonary_one.keys())       #it will check if the value present in keys of the dictonary
print("key1" in dictonary_one.values())     #it will check if the value present in the value in the dictonary