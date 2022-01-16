# file open has the default parameter called mode="r" that only allow us to read the file
# but if we want to make changes or write into the file we simply make the mode="w / r / r+"

# mode="r+"
# write 
with open("test.txt", mode="r+") as my_file:        #r+means you can read and write into the file at the same time
    mytext = my_file.write("-hee-")
    print(mytext)
    # but the main problem here is that it start writing at the point the cursor is and if something in that position it will rewrite it 


# mode="a"
# to write from the last index of the file we use the append inside the mode mode="a"
with open("test.txt", mode="a") as myfile:
    my_text = myfile.write(" * is it at the last position in the file")


# the difference between the two mode a & r+ 
# r+ start the writing at the curcer last position
# a writes at the end of the file


# mode="w"      #it will only write the file and replace with all the content of the file
with open("test.txt", mode="w") as myfile3:
    mytext3 = myfile3.write(" oppps accedently delete all the content of the data ")
    # also when we are using the w mode if the file is not present it will create the file automatically with that name



# how to access file into another folder
with open("folder1/test2.txt", mode="r") as myfile4:
    mytext4 = myfile4.read()
    print(mytext4)
    # it will go to the folder pick the test2.txt and it will read it for you 
    # and remember that if you want to goi back you can use ..