from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "Q)uit, C)hoose taxi, D)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print(f"Let's drive!\n{MENU}")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            pass

        elif choice == "d":
            pass

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Bill to date: ${total_bill:.2f}\nTaxis are now:\n" + "\n".join([f"{i} - {taxi}" for i, taxi in enumerate(taxis)]))


main()
