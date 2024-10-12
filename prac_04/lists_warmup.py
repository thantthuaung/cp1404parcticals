numbers = [3, 1, 4, 1, 5, 9, 2]
"""
numbers[0] 
value = 3

numbers[-1]
value = 2

numbers[3]
value = 1

numbers[:-1]
value = [3, 1, 4, 1, 5, 9]

numbers[3:4]
value = [1]

5 in numbers
True

7 in numbers
False

"3" in numbers
False

numbers + [6, 5, 3]
value = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""
# 1.
numbers[0] = "10"

# 2.
numbers[-1] = 1

# 3.
print(numbers[2:])

# 4.
print(9 in numbers)