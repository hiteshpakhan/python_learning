# 1# expression vs sentence
# variable_age = 3 / 2
# here the 3/2 is called as the expression 
# and the entire line of code we called it as the statement 

# 2# Escape sequences    
# (\) whatever comes after this slash is a str consedered in python
# (\n) its a new line
# (\t) its a tab


# 3# formatted string
name = "hitesh"
age_string = "21"
age_int = 21
print("hi my name is " + name + " and i am " + age_string + " years old")     #this is when you want to mearge strings with strings
print(f"hi my name is {name} and i am {age_int} years old")             #this is when you want to merge the string with the int or any other two or more than two data type

# 4# variable name
variable_name = "data" # you can give the underscore in the variable name 
# variable-name = "data" # you can not add the minus sign in the variable name

# 5# .format()

# 6# input()
# imp whatever your inputing it always comes in the string so you better convert it at the start
birth_year = input("what is your birth year = ")
age = 2021 - int(birth_year)
print(f"your born year is {birth_year} and your age is {age}")