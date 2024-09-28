mini_variable = 7
user_input = input("Enter password: ")
while len(user_input) != mini_variable:
    print("Invalid password")
    user_input = input("Enter password: ")
print("*"*len(user_input))
