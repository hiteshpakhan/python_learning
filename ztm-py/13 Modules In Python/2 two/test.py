import sample_pkg.pkg1          #it will automatically print the name and the location of the imported file
print("hi the upper name is the name of the file that we imported")

print(__name__)     #it will print __main__ if we run this file
#__name__ is returns you the location and the name of the file
# but if it is the file that we are running then it will return thye __main__ as the file name

# to check if we are inside the file of the running we can use the __name__ == "__main__"
# for example
if __name__ == "__main__":
    print("yes we are inside the file that currently running the poject")