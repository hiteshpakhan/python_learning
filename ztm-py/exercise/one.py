# password checker

username = input("username : ")
password = input("password : ")
size = len(password)
hidden_password = "*" * size
print(f"username is {username} and your password {hidden_password} length is {size} letters long")