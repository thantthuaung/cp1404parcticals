number_of_special = 0
password = "t2000"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
for character in password:
    if character in SPECIAL_CHARACTERS:
        number_of_special += 1
print(len(password))