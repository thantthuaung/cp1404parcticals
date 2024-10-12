# filename = input("Enter file name: ")
# in_file = open(filename, 'r')
# in_file.close()

# name = input("Enter Name: ")
# with open("name.txt", "w") as file:
#     print(name, file=file)
# print("done")

# names = ['teddy', 'mcc', 'mal', 'kwy_thr']
# for name in names:
#     with open(name, "w") as out_file:
#         print(name, file=out_file)

file_name = "counrty_name.txt"
with open(file_name, "r") as in_file:
    for line in (0, file_name, 2):
        print(f"{in_file.readline().strip()} was born in {in_file.readline().strip()}")

