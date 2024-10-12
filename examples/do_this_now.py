# names = ["Ada", "Alan", "Bill", "John"]
# print(", ".join(names))
# names_to_remove = input("Who do you want to remove? ")
#

# while names_to_remove != "":
#     if names_to_remove in names:
#         names.remove(names_to_remove)
#     else:
#         print("Invalid Name. It is not in the list.")
#     print(", ".join(names))
#     names_to_remove = input("Who do you want to remove? ")
# print("Finished")

# while names_to_remove != "":
#     try:
#         names.remove(names_to_remove)
#     except ValueError:
#         print("Invalid Name. It is not in the list.")
#     print(", ".join(names))
#     names_to_remove = input("Who do you want to remove? ")
# print("Finished")

# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
#
# def get_numbers():
#     list_of_numbers = []
#     input_number = int(input(">>> "))
#     while input_number != "":
#         list_of_numbers.append(input_number)
#     return list_of_numbers
#
#
# def square_numbers(numbers):
#
#     return [number ** 2 for number in numbers]
#
# def display_numbers(numbers):
#     print()


data = [['Derek', 7],['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
name_width = max((len(pair[0]) for pair in data))
score_width = max((len(str(pair[1])) for pair in data))

for pair in data:
    name, score = pair
    print(f"{name:{name_width}} = {score:{score_width}}")
# for i in data:
#     for j in i:
#         print(f"{j} = ")
# print()
