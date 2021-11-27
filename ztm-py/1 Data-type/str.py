# 1
# str represent the string in python
# we put any str into the single or double cotes "" ''
# you can use _ to declare the str name but you can never use the (-) minus sign in between the name of the variable str  
print(type("skjfhsdfnvdnfv kjbdkbfv"))   # it will give you the type of str
# for long string you can used the ''' ''' three cotes
print(type('''tuhejnf ksjdfjdfv
fju evs f
kesrg rb vr 
ekrjv j fv
se'''))         # it will also give you the type str


# 2 string concatination
# you can also perforn some experiment on the str  
first_name = "hitesh"
last_name = "pakhan"
full_name = first_name + " " + last_name
print(full_name)


# 3 string indexes:-
big_string = "ABCDFGA566@GMAIL.COM"
#             012345678901234567890

index_1 = big_string[1]      
print(index_1)        #it will give string that at the index 1 : b
index_m1 = big_string[-1]  #it is in the minus index      
print(index_m1)       #it will give the index string from the last index -1: m 


# 4 string indexes [start:stop]
index4_11 = big_string[4:11]
print(index4_11)        #it will give the output FGA566@


# 5 string indexes [start:stop:stepover]
index4_11_2 = big_string[4:11:2]
index4_11_3 = big_string[4:11:3]
print(index4_11_2)        #it will give the output FA6@
print(index4_11_3)        #it will give the output F5@
# as you can see it stepover the strings by 2 and 3
index_3 = big_string[::-3]
print(index_3)


# 6 string indexes 
index0_len = big_string[0:len(big_string)]      #0-length of the string
index0_len_4 = big_string[0:len(big_string)-4]      #0-length of the string without 4 last digit
print(index0_len)
print(index0_len_4)
# hufhuhfkvabkbfk


