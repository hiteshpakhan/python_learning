# time

from time import time

def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()         # time always measure the time in the miliseconds
        result = fn(*args, **kawrgs)
        print(args,kawrgs)
        t2 = time()
        print(f"took {t2-t1} ms")
        # return result
    return wrapper          # its compulsary to return

@performance
def long_time():
    for i in range(100):
        i*5
        print(i)

long_time()