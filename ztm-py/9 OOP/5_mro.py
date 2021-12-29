class A():
    num = 10

class C(A):
    num = 1

class B(A):
    num = 11
    
class D(B,C):
    pass

print(D.num)        #it gives the value we define at the C class and ignore the value at the A class

# to check the path of the execution of the inheritance you can check with the .mro()
print(D.mro())