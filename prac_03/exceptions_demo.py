"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when the user inputs a String value.
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when the denominator entered by the user is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, I can change the code with the error checking to avoid the possibility of a ZeroDivisionError.
    I will use If ... else... statement.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero.")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
