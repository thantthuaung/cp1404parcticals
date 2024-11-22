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

class Monitor:
    def __init__(self, model: str, width: int, height: int):
        self.model = model
        self.width = width
        self.height = height

    def get_resolution(self) -> tuple:
        return self.width, self.height

    def get_total_pixels(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __str__(self):
        return f"{self.model} has {self.get_total_pixels()} {self.get_resolution()} resolution"


model1 = Monitor("mac", 1080, 2080)
print(model1)
model2 = Monitor("other", 1080, 2080)
print(model2)
print(model1 == model2)

