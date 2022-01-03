# try
# except
# else



# try and except
        # age = int(input("what is your name"))   #but if here i give the input in string it will thorugh an error
        # print(age)
# still if you want to run the upper programe you can do it by error handling try except
try:
    age = int(input("what is your age"))
    print("1 yor age is : ",age)
except:                             # if the try gives an error then the the except block will run
    print("please enter only number")

# if you want to continussly take input until the user give the write input 

while True:
    try:
        age2 = int(input("what is your age2 : "))
        print("2 yor age2 is : ",age2)
        break
    except:
        print(" -- ! please enter only number --")

# or
# you can use this method also

# else
while True:    
    try:
        age3 = int(input("what is your age3 : "))
        print("3 yor age3 is : ",age3)
    except:
        print(" -- ! please enter only number --")
    else:                               # when the try block execute then the else block will execute 
        print("thanks")
        break                           # these breack will be breake the while statement