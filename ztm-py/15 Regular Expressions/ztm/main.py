# regular expression are very useful in validition ,like chacking email, finding string in sentences
# python comes regular expression module

my_string = "find the string inside me"

print("find" in my_string)        #output:- True
#this is the normal way of doing search inside of text
# regular expression is more more powerful than this method

# to import regular expression
import re


# .search()
print(re.search("find", my_string))     # output:- <re.Match object; span=(0, 4), match='find'>
# it will give us the output in the form of object with the index of start and ending of the string

# to store the output 
a = re.search("find", my_string)

print(a.span())     #output:-  (0, 4)
print(a.start())    #output:-  0
print(a.end())      #output:-  4
print(a.group())    #output:-  find     #it will tell you what was the matched


# you can also store your searching string by compile
same_pattern = re.compile("find")
print(same_pattern.search(my_string))
b = same_pattern.search(my_string)      
print(b.span())
print(b.start())
print(b.end())
print(b.group())



# .findall()

string2 = "hee this is the second string hee heee"
pattern2 = re.compile("hee")
print(pattern2.findall(string2))        #output:- ['hee', 'hee', 'hee']

# .fullmatch()
print(pattern2.fullmatch(string2))      #output:- None  #to get the result it has to be a fully matched

# .match()
print(pattern2.match(string2))          #output:- <re.Match object; span=(0, 3), match='hee'>