# IMP

even = []
def higest_even(li):
    higest = 0              #here we have to define the variables inside the function or we can not access it properly.
    for each in li:
        if each % 2 ==0:
            even.append(each)
    for every in even:
        if every > higest:
            higest = every
    print(f"higest even number in the list is {higest}")

higest_even([154,1541,15,454,54,5158,45,1584])