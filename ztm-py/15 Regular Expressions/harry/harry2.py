import re
para = '''@kjbkb. 0 Groups. kjbkb. 
2Recordings0Songs0Favorites0Followers0Following. 
RecordingsSmuleGuitar!Magic PianoAutoRap. 
kjbkb has no recordings.'''

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
patt4 = re.compile(r"ings\.$")      #if your string has a . you can use the \
obj_store4 = patt4.finditer(para)
for l in obj_store4:
    print(l)        #output:- <re.Match object; span=(138, 142), match='ings'>


# *
print("****")
patt5 = re.compile(r"in*")      #here you are saying that you want g and if s comes after that zore or more than zero times
obj_stroe5 = patt5.finditer(para)
for m in obj_stroe5:
    print(m)
    # output:-
# <re.Match object; span=(33, 35), match='in'>
# <re.Match object; span=(49, 50), match='i'>
# <re.Match object; span=(70, 72), match='in'>
# <re.Match object; span=(82, 84), match='in'>
# <re.Match object; span=(93, 94), match='i'>
# <re.Match object; span=(101, 102), match='i'>
# <re.Match object; span=(105, 106), match='i'>
# <re.Match object; span=(138, 140), match='in'>