# finally
# finally executes after everithing has been executed 
# it will also executes when any error will occore or will not be occor

while True:    
    try:
        age3 = int(input("what is your age3 : "))
        print("3 yor age3 is : ",age3)
    except:
        print(" -- ! please enter only number --")
    else:                               # when the try block execute then the else block will execute 
        print("thanks")
        break
    finally:
        print("here the finnaly will be executes after everithing has been executes")

# dont think that finally has no use in the prigramming  
# finally can be very usefull in th esenario like these 
# when we are count the no of user try to login and may some of the users are leaving the interface in the middel



# for testing purpuse you can also raise a new specific artifical error in your programe

# raise

while True:
    try:
        agevar = input("enter your age here : ")
        print(agevar)
        raise ValueError("hee this is the my own created value error")
    except ValueError as cat:
        print(f"hee pal you got som value error here =======> {cat}")
    else:
        break
    finally:
        print("here you go this is the finally")