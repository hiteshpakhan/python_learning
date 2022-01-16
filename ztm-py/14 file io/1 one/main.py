# file i/o
# means we will take some input from outside our python file and give something as output outside our python file

# open()
var_file = open("test.txt") # to open the file
print(var_file)

# .read()
print(var_file.read())      # to read the file

print(var_file.read())  #here you can face the problem when you want to read the filer again
# it will happen because you already read the file once and the curser is at the last index of the file
# and to move the cursur again at the 0thg index you have to put by using .seek()

# .seek()
var_file.seek(0)
print(var_file.read())      #now you can again able to read the file

# .readline()
var_file.seek(0)
print(var_file.readline(),"line 1")
print(var_file.readline(),"line 2")
print(var_file.readline(),"line 3")
print(var_file.readline(),"line 4")

# .readlines()
var_file.seek(0)
print(var_file.readlines(),"all lines")     #it will give you all the lines inside the list


# now that you open the file its time to close it 
# and to close the file you use the .close()
var_file.close()