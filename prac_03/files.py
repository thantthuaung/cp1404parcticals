user_name = input("Enter your name: ")
out_file = open("name.txt", 'w')
out_file.write(user_name)
out_file.close()

file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")

with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    total_number = first_number + second_number
print(total_number)

with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line.strip())
print(total)
