from functools import reduce

# Implementation of Functional Programming Tools

# Example 1: Filtering Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Example 2: Reducing a List of Numbers
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", sum_of_numbers)
