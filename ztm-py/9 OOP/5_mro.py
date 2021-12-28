class A():
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

print(D.num)        #it gives the value we define at the C class and ignore the value at the A class
