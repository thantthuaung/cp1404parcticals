"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU = """(H)ello
(G)oodbye
(Q)uit"""
user_name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {user_name}")

    elif choice == "G":
        print(f"Goodbye {user_name}")

    else:
        print(f"Invalid Choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
