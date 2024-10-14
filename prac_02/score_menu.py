import random
MENU = ">(G)et a valid score (must be 0-100 inclusive)\n>(P)rint result\n>(S)how stars\n>(Q)uit "

def main():
    score = 0
    print(MENU)
    get_input = get_valid_input()
    while get_input != "Q":
        if get_input == "G":
            score -= score
            score += get_valid_score()
        elif get_input == "P":
            result = determine_result(score)
            print(result)

        elif get_input == "S":
            print("*"*score)
        else:
            print("Invalid Choice")
        print(MENU)
        get_input = get_valid_input()
    print("Farewell.")


def get_valid_score():
    score_input = int(input("Enter score: "))
    while score_input < 0 or score_input > 100:
        print("invalid score")
        score_input = int(input("Enter score: "))
    return score_input


def get_valid_input():
    get_input = input("Enter choice: ").upper()
    while get_input == "":
        print("Invalid")
        get_input = input("Enter choice: ").upper()
    return get_input

def determine_result(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()