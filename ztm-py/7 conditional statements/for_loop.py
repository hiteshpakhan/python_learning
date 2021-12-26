# for

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