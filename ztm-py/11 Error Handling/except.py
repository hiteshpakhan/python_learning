# except can also used for act on a specific errors
while True:
    try:
        age = int(input("what is your age : "))
        10/age
    except ValueError:              # you can give the name of the error and type the specific warning
        print("warning : please enter a number")
    except ZeroDivisionError:
        print("warning : give another value can not divided by zero")
    else:
        break

# 2nd example
def sum(num1, num2):
    try:
        return num1 + num2
    except:
        print("something is wrong")

print(sum("3", 5))        