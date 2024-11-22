def main():
    mini_variable = 7
    user_input = get_password(mini_variable)
    print_output(user_input)


def print_output(user_input):
    print("*" * len(user_input))


def get_password(mini_variable):
    user_input = input("Enter password: ")
    while len(user_input) != mini_variable:
        print("Invalid password")
        user_input = input("Enter password: ")
    return user_input


main()