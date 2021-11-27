#methods are similer to the function in its own way but they are owened by something

# string methods 

# there are many string methods that we can used specifially used on the string
# string methods uselly have the . at the front and brackets at the end

# but the most imp thing string method will not chang the main string but it create the new that you can assign to the new variable 

quote = "To Be Or not to be"

print(quote.upper())    # it will give you the output in the capatile
# op:-
# TO BE OR NOT TO BE

print(quote.capitalize())       #it will convert the first letter of the string capital
# op:-
# To be or not to be

print(quote.lower())        #it will convert all the string into smallcase
# op:-
# to be or not to be 

print(quote.find("be"))         #it will find the string you given in the string you want to find and give you the starting index of the string
# op:-
# 16

print(quote.replace("be","m"))      # it will replace the be to the m at the big string
# op:-
# To Be Or not to m

# you can also create the new variable and assign the modifyed string to it and stored it 
quote2 = quote.replace("be","replace")
print(quote2)           
# op:-
# To Be Or not to replace

# these upper the some of the all string methods but there are more you can search it online if you want 