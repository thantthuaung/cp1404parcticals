"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""

CONSTANT_SALES = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < CONSTANT_SALES:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"User's bonus: {bonus}")
    sales = float(input("Enter sales: $"))
print("thank you")
