import re
para = '''@kjbkb. 0 Groups. kjbkb. 
2Recordings0Songs0Favorites0Followers0Following. 
RecordingsSmuleGuitar!Magic PianoAutoRap. 
kjbkb has no recordings'''

# .
patt = re.compile(r".")     #by using . you are saying you want any characters
obj_store = patt.finditer(para)
for i in obj_store:
    print(i)        #it will output all the character in the form of obj



# 
patt2 = re.compile(r".ing") #now your saying that you want any characters that has "ing" after them
obj_store2 = patt2.finditer(para)
for j in obj_store2:
    print(j)

# output
# <re.Match object; span=(32, 36), match='ding'>
# <re.Match object; span=(69, 73), match='wing'>
# <re.Match object; span=(81, 85), match='ding'>
# <re.Match object; span=(137, 141), match='ding'>


# ^ starts with
patt3 = re.compile(r"^@k")          #it will check if the hole para start with given string then only it will return the obj
obj_store3 = patt3.finditer(para)
for k in obj_store3:
    print(k)        #output:- <re.Match object; span=(0, 2), match='@k'>



# $ end with
print("****")
patt4 = re.compile(r"ings$")
obj_store4 = patt4.finditer(para)
for l in obj_store4:
    print(l)        #output:- <re.Match object; span=(138, 142), match='ings'>