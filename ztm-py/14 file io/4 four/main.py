# when you are using the file i/o 
# you shoud use it inside the try and except block 
# sometimes when the file not found errors may occor

try:
    with open("some file", mode="r") as myfile:
        print(myfile.read())
except FileNotFoundError as err:
    print("sorry it seens that there is not any file with that name")
    raise err