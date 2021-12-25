# tuple ()
# .count()
# .index()



# tuple ()
# tuple is similer to the list 
# you can not perform sort or reverse like operations on the tuple

tuple_one = (1,2,3,4,5,5,5)
print(tuple_one)
print(tuple_one[1])
print(tuple_one[1:3])

a,b,*other = tuple_one
print(a)
print(b)
print(other)

# tuple_one[1] = 56     #it will give an error because tuple not support item assignment 

print(5 in tuple_one)

# tuple methods

# .count()
print(tuple_one.count(5))       #it will count how many times the value has occoured in the tuple

# .index()
print(tuple_one.index(5))       #it will give the index where given value occore first