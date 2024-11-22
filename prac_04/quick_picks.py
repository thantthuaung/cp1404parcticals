import random
TOTAL_RANDOM_NUMBER = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

quick_pick = int(input("How many quick pick? "))
for i in range(quick_pick):
    random_numbers_list = []
    for j in range(TOTAL_RANDOM_NUMBER):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in random_numbers_list:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_numbers_list.append(number)
        random_numbers_list.sort()
    print(' '.join(f"{str(number):2}" for number in random_numbers_list))
