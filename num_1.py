import random

# a
list_random: list[bool] = [random.choice([True, False]) for _ in range(3)]
print(list_random)
# b
print(list_random, "all()", all(list_random))
# c
print(list_random, "any()", any(list_random))
# d
print(list_random, " not all()", not all(list_random))
# e
print(list_random, "not any()", not any(list_random))
# f
numbers: list[int] = [random.randint(-2, 2) for _ in range(5)]
print(numbers)
# g
print("all numbers in the list are different from - 0:", not any(number == 0 for number in numbers))
# h
print("The list has at least one number equal to 0:", any(number == 0 for number in numbers))

# i
print("all numbers in the list equal to 0:", all(number == 0 for number in numbers))
# j
print("The list has at least one number equal to 0:", any(number == 0 for number in numbers))
