# from random import randint
#
# low_number = int(input("Enter the low number: "))
# high_number = int(input("Enter the low number: "))
#
# while high_number < low_number:
#     print("Invalid High Number")
#     high_number = int(input("Enter the low number: "))
#
# n = randint(low_number, high_number)
# print(f"The random number is {n}")
# print(f":)"*n, end=" ")

import random
MENU = "(S)tart\n(R)andom name\n(Q)uit "

def main():
    user_name = ""
    print(MENU)
    get_input = get_valid_input()
    while get_input != "Q":
        if get_input == "S":
            user_name = get_valid_name()
        else:
            new_name = random.shuffle(list(user_name))
            print(f"----------\n{new_name}\n----------")
        get_input = get_valid_input()
    print("Farewell.")
def get_valid_input():
    get_input = input("Enter choice: ").upper()
    while get_input == "":
        print("Invalid")
        get_input = input("Enter choice: ").upper()
    return get_input

def get_valid_name():
    user_name = input("Enter your name: ").upper()
    while user_name == "":
        print("Invalid")
        user_name = input("Enter your name: ").upper()
    return user_name
main()