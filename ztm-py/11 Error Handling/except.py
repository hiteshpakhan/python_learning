while True:
    try:
        age = int(input("what is your age : "))
        10/age
    except ValueError:              # you can give the name of the error and type the specific warning
        print("warning : please enter a number")
    except ZeroDivisionError:
        print("warning : give another value can not divided by zero")
    else:
        print("thank you")
        break