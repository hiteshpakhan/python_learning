# to find the duplicates and make the saperates list, one with the duplicates and one without duplicates
# some_list = ["a","b","c","b","d","n","m","m"]

# duplicates = []
# new_set = set([])

# for each_item in some_list:
#     for _ in new_set:
#         if _ == each_item:
#             duplicates.append(_)
#     new_set.add(each_item)

# print(duplicates)
# new_list = list(new_set)
# new_list.sort()
# print(new_list)

some_list = ["a","b","c","b","d","n","m","m"]

duplicates = []
new_set = set([])

for each_item in some_list:
    if each_item in new_set:
        duplicates.append(each_item)
    new_set.add(each_item)

print(duplicates)
new_list = list(new_set)
new_list.sort()
print(new_list)