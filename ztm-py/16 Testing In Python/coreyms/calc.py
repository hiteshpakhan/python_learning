def function1(num1, num2):
    print("this is the first number : ",num1)
    print("this is the first number : ",num2)
    return num1

def divide(x, y):
    if y == 0:
        raise ValueError("cannot divide by zero")
    return x / y