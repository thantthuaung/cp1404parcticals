from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another guitar", 2013, 10000)
print(gibson)
print(another_guitar)
print(f"\n{gibson.name} get_age() - Expected {gibson.get_age()}. Got {gibson.get_age()}")
print(f"{another_guitar.name} get_age() - Expected {another_guitar.get_age()}. Got {another_guitar.get_age()}")
print(f"{gibson.name} is_vintage - Expected {gibson.is_vintage()}. Got {gibson.is_vintage()}")
print(f"{another_guitar.name} is_vintage - Expected {another_guitar.is_vintage()}. Got {another_guitar.is_vintage()}")
