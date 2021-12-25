# set {}
# set is an unordered collection of an unique elements
# set does not support item indexing

my_set = {1,1,2,3,4,4,5,6,6,7,7,8,8}
print(my_set)   #it will give the output {1, 2, 3, 4, 5, 6, 7, 8} it will automatically remove all the duplecate elements

set_two = {1,2,3,4,5}
set_two.add(100)
print(set_two)

# print(set_two[2]) it will give an error because set does not support indexing
# if you want to check something in the set you can use in
print(1 in set_two)

print(len(set_two))

# here if we have to convert the normal list into a list that has no duplicate values
list1 = [1,1,2,3,3,4,5,5]
set1 = set(list1)
list2 = list(set1)
print(list2)  
# op: [1, 2, 3, 4, 5]   we successfully made a list with no duplicates

new_set = set_two.copy()
print(new_set)


# set methods

set_first = {1,2,3,4,5}
set_second = {4,5,6,7,8,9,10}

# .difference()
print(set_first.difference(set_second))  # op: {1, 2, 3}

# .discard()
set_second.discard(10)    #it will discard the 10 from the set
print(set_second)         #op: {4, 5, 6, 7, 8, 9}

# .difference_update()
set_first.difference_update(set_second)  #it will remove the elements that are in another set
print(set_first)                         #op: {1, 2, 3} 

# we will create new variable for the further operations
setFirst = {1,2,3,4,5}
setSecond = {4,5,6,7,8,9,10}

# .intersection()
print(setFirst.intersection(setSecond))  #op: {4, 5}  #it will give you all the common element in both of them
# there is a short form of intersection
print(setFirst & setSecond)              #op: {4, 5}

# .isdisjoint()
print(setFirst.isdisjoint(setSecond))    #op: False   #it will see if there is anything in common if there then it will give the false

# .union
print(setFirst.union(setSecond))         #op: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}   #it will combine two set without duplicating any element
# there is even short form of doing form 
print(setFirst | setSecond)              #op: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# we will create new variable for the further operations
new_set_one = {4,5}
new_set_two = {4,5,6,7,8,9,10}

# .issubset()
print(new_set_one.issubset(new_set_two))        #True #it will check is it is an subset of another set

# .issuperset()
print(new_set_one.issuperset(new_set_two))      #false #it will check is it is an superset of another set
print(new_set_two.issuperset(new_set_one))      #true