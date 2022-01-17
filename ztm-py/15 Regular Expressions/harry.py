# this specific is not the part of ztm cource it is from harry python cource from youtube file is
import re

mystr = '''@kjbkb. 0 Groups. kjbkb. 
2Recordings0Songs0Favorites0Followers0Following. 
RecordingsSmuleGuitar!Magic PianoAutoRap. 
kjbkb has no recordings.'''


pattern1 = re.compile(r"Recording")
# .finditer()
a = pattern1.finditer(mystr)
print(a)
# output:- <callable_iterator object at 0x000002C3138ECF10>

for i in a:
    print(i)
# <re.Match object; span=(27, 36), match='Recording'>
# <re.Match object; span=(76, 85), match='Recording'> 

# as you can see that there an object that holds the data in group