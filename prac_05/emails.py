"""
Emails
Estimate: 20 minutes
Actual:   29 minutes
"""


def main():
    EMAIL_AND_NAME = {}
    email_with_com = input("Email: ")
    edit_gmail_name(EMAIL_AND_NAME, email_with_com)
    for key, value in EMAIL_AND_NAME.items():
        print(f"{key} ({value})")


def edit_gmail_name(EMAIL_AND_NAME, email_with_com):
    while email_with_com != "":
        email_without_com = email_with_com.split("@")
        name_from_email = email_without_com[0].split(".")
        name = " ".join(name_from_email).title()
        determine_name_y_or_n(EMAIL_AND_NAME, email_with_com, name)
        email_with_com = input("Email: ")


def determine_name_y_or_n(EMAIL_AND_NAME, email_with_com, name):
    yes_or_no_input = input(f"Is your name {name}? (Y/n) ").lower()
    if yes_or_no_input == "y" or yes_or_no_input == "":
        EMAIL_AND_NAME[name] = email_with_com
    else:
        new_name = input("Name: ").title()
        EMAIL_AND_NAME[new_name] = email_with_com


main()
