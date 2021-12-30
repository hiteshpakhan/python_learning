# list comprehension

# normal method of using the list
my_list = []

for char in "student":
    my_list.append(char)

print(my_list)

# by using list comprehension
# this is the shortcut method of using list

my_list2 = [char2 for char2 in "student 2"]
print("\n",my_list2)
my_list3 = [num*2 for num in range(0, 100)]
print("\n",my_list3)
my_list4 = [num2**2 for num2 in range(0, 100) if num2 % 2 == 0]             # imp 
print("\n",my_list4)
my_list5 = [num3 for num3 in range(0, 100) if num3 % 2 == 0]             
print("\n",my_list5)