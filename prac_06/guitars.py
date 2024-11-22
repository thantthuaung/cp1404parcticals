from prac_06.guitar import Guitar
print(f"My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = input("Cost: ")
    my_guitar = Guitar(name, year, float(cost))
    guitars.append(my_guitar)
    print(f"{my_guitar} added.\n")
    name = input("Name: ")
print(f"\n ... snip ...\n\nThese are my guitars:")
# name_max_width = max(len(guitar.name) for guitar in guitars)
# cost_max_width = max(len(str(guitar.cost)) for guitar in guitars)
for i, guitar in enumerate(guitars, 1):
    vintage = "(vintage)"
    if guitar.is_vintage():
        # print(f"Guitar{i}: {guitar.name:>{name_max_width}} ({guitar.year}), worth $ {guitar.cost:>{cost_max_width},.2f}{vintage}")
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")
    else:
        # print(f"Guitar{i}: {guitar.name:>{name_max_width}} ({guitar.year}), worth $ {guitar.cost:>{cost_max_width},.2f}")
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")
