# this specific is not the part of ztm cource it is from harry python cource from youtube file is
import re

mystr = '''@kjbkb. 0 Groups. kjbkb. 
2Recordings0Songs0Favorites0Followers0Following. 
RecordingsSmuleGuitar!Magic PianoAutoRap. 
kjbkb has no recordings.'''

pattern1 = re.compile(r"Recording")
a = pattern1.finditer(mystr)
print(a)
# output:- <callable_iterator object at 0x000002C3138ECF10>