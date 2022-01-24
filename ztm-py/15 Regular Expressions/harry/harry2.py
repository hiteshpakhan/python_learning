import re
para = '''@kjbkb. 0 Groups. kjbkbkjbkb. 
2Recordings0Songs0Favorites0Followers0Following. 
RecordingsSmuleGuitar!Maginnnnnc PianoAutoRap. 
kjbkb has kjvvhbh no recordings.'''

# . 
# any character
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


# ^ 
# starts with
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
# zero or more than zero
patt5 = re.compile(r"in*")      #here you are saying that you want g and if s comes after that zore or more than zero times
obj_store5 = patt5.finditer(para)
for m in obj_store5:
    print(m)

# output:-
# <re.Match object; span=(33, 35), match='in'>
# <re.Match object; span=(49, 50), match='i'>
# <re.Match object; span=(70, 72), match='in'>
# <re.Match object; span=(82, 84), match='in'>
# <re.Match object; span=(93, 94), match='i'>
# <re.Match object; span=(101, 102), match='i'>
# <re.Match object; span=(101, 107), match='innnnn'>
# <re.Match object; span=(110, 111), match='i'>
# <re.Match object; span=(143, 145), match='in'>


# + 
# one or more than one
patt6 = re.compile(r"in+")
obj_store6 = patt6.finditer(para)
for n in obj_store6:
    print(n)
# output:-
# <re.Match object; span=(33, 35), match='in'>
# <re.Match object; span=(70, 72), match='in'>
# <re.Match object; span=(82, 84), match='in'>
# <re.Match object; span=(101, 107), match='innnnn'>
# <re.Match object; span=(143, 145), match='in'>


# {} 
# exactily the specified number of occurrence
patt7 = re.compile(r"in{5}")
obj_store7 = patt7.finditer(para)
for o in obj_store7:
    print(o)
# output:-
# <re.Match object; span=(101, 107), match='innnnn'>



# () 
# capture and group
patt8 = re.compile(r"(kjbkb){2}")   #it will check hole kjbkb 2 times
obj_store8 = patt8.finditer(para)
for p in obj_store8:
    print(p)
# output:-
# <re.Match object; span=(18, 28), match='kjbkbkjbkb'>



# | 
# either or
patt9 = re.compile(r"Re|kj")    #it will give you all the strings that contain kj or that contain the Re
obj_store9 = patt9.finditer(para)
for q in obj_store9:
    print(q)
# output:-
# <re.Match object; span=(1, 3), match='kj'>
# <re.Match object; span=(18, 20), match='kj'>
# <re.Match object; span=(23, 25), match='kj'>
# <re.Match object; span=(32, 34), match='Re'>
# <re.Match object; span=(81, 83), match='Re'>
# <re.Match object; span=(129, 131), match='kj'>



# \A 
# returns the match if the given char is the begining of the string
patt10 = re.compile(r"\A@kj")
obj_store10 = patt10.finditer(para)
for r in obj_store10:
    print(r)
# output:-
# <re.Match object; span=(0, 3), match='@kj'>



# \b 
# returns the match if the given string is at the begining of the any words in the paragraph 
print("****")
patt11 = re.compile(r"\bkj")
obj_store11 = patt11.finditer(para)
for s in obj_store11:
    print(s)
# output:-
# <re.Match object; span=(1, 3), match='kj'>
# <re.Match object; span=(18, 20), match='kj'>
# <re.Match object; span=(129, 131), match='kj'>
# <re.Match object; span=(139, 141), match='kj'>


# similery if we put the \b at the end of the given string it will find the words that ending with the given string

# \B
# \d
# \D
# \s
# \S
# \w
# \W
# \Z 