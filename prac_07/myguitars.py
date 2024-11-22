from prac_07.guitar import Guitar
def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    store_guitar_in_list(guitars, in_file)
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def store_guitar_in_list(guitars, in_file):
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)

main()
