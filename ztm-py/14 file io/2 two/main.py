# before we seen that how to open and close the file
# but by using with open we dont have to worry about the closing of a file 

# with 
# as


with open("test.txt") as my_file:
    print(my_file.readlines())