# for
# in
# range()
# enumerate()

for item in "abcdefg":
    print(item)                             #it allows us to ittrate each item inside element

for item in {"a", "b", "c", "d", "e", "f"}:
    print(item)             #set never understand the sequence of the items 

user = {
    "name" : "hitesh",
    "rollno" : 21,
    "branch" : "CSE" 
}
for key, value in user.items():
    print(key," : ",value)          #imp you can access the keys and values ike this

my_list = [1,2,3,4,5,6,7,8,9,10]
total = 0
for each_item in my_list:
    total += each_item

print(total)

# range(stop)
# range(start, stop)
# range(start, stop, stepover)
print(list(range(5,15)))
print(list(range(10)))
print(list(range(1,20,2)))   #defaule stepover is 1
print(list(range(10,0,-1)))

# enumerate

for i,v in enumerate(["a","b","c","d","e","f"]):
    print(i, " : ", v)                          #by enumerator you can find the indexes with the value


# if we has to find the index of 50 in the list
for index1,value1 in enumerate(list(range(100))):
    if(value1==50):
        print(f"index of 50 is : {index1}")