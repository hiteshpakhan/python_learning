print("before importing modules file into this file\n")
import modules
print("\nafter importing the file")

print("\n",modules.mul(2,3))        # you can also use the stuf from the imported file
# as you can see that it create2d a new __pycache__ folder



# but if your file is in the another folder that means that folder is called as the package and to import it you have to use . 
import folder1.example

# this is the second folder that you created inside the pycharm
import folder2.example2