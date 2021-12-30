# 1 list slicing
# sorting the dictionary by their value by their 
list1 = [(0,2),(4,3),(9,9),(10,-1)]
list1.sort(key = lambda x: x[1])
print(list1)


# giving the list item the values and making it dictionary
my_dict = {num : num**2 for num in [1,2,3]}
print(my_dict)


# finding the duplicates in the list
some_list = ["a","b","d","c","a","d","d","e","f"]

duplicates = list(set(x for x in some_list if some_list.count(x) > 1))

print(duplicates)