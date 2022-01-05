# febonacci serise
# for example : 0 1 1 2 3 5 8 13 21 34

def fib(number):            # here the number will be the count that deside how many fibonicci numbers you want 
    a = 0 
    b = 1
    for i in range(number):
        yield a             # you have to understand what is yield so give it a shot
        temp = a
        a = b
        b = temp + b

for x in fib(10):
    print(x)