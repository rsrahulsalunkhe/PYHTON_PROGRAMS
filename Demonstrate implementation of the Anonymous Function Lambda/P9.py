# Implementation of Anonymous Function (Lambda)

# Example 1: Simple Addition
addition = lambda x, y: x + y
result = addition(5, 3)
print("Addition:", result)

# Example 2: Square of Numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared Numbers:", squared_numbers)

# Example 3: Sorting a List of Tuples
students = [("John", 25), ("Jane", 20), ("Alice", 22), ("David", 19)]
students.sort(key=lambda x: x[1])
print("Sorted Students:", students)
