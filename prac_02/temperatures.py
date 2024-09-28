"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    print("C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit")
    choice = input(">>> ").upper()


    def calculate_celsius_to_fahrenhit():
        global celsius, fahrenheit
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")


    def calculate_fahrenheit_to_celsius():
        global fahrenheit, celsius
        fahrenheit = float(input("Fahrenheit: "))
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")


    while choice != "Q":
        if choice == "C":
            calculate_celsius_to_fahrenhit()
        elif choice == "F":
            calculate_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
main()
