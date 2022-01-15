from collections import Counter, defaultdict, OrderedDict

# counter
my_list = [1,2,3,4,5,5,5,3,8,8]
print(Counter(my_list))

my_sentence = "hbd vvv gfddf v vevdv de erdg b frsd"
print(Counter(my_sentence))

# defaultdict
my_dictionary = defaultdict(lambda: 4, {"a":1, "b":2, "c":3})
print(my_dictionary["d"])

# OrderedDict
d1 = OrderedDict()
d1["a"]=1
d1["b"]=2

d2 = OrderedDict()
d2["a"]=1
d2["b"]=2

print(d1 == d2)
print(d1, "\n", d2)