"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
def main():
    score = int(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_number = random.randint(0,100)
    result_for_random_number = determine_result(random_number)
    print(result_for_random_number)

def determine_result(score):
    if score < 0 or score > 100:
        return"Invalid score"
    elif score < 50:
        return"Bad"
    elif score < 90:
        return"Passable"
    else:
        return"Excellent"
main()