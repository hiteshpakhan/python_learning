# password checker

username = input("username : ")
password = input("password : ")
size = len(password)
hidden_password = "*" * size
print(f"{username}, your password, {hidden_password}, is {size} letters long")