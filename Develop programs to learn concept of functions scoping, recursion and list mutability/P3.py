# Function Scoping, Recursion, and List Mutability Example

# Global variable
global_var = 10

# Function with local variable
def my_function():
    local_var = 20
    print("Local variable:", local_var)
    print("Global variable within function:", global_var)

# Calling the function
my_function()

# Accessing global variable outside the function
print("Global variable outside function:", global_var)

# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculating factorial of a number
num = 5
result = factorial(num)
print("Factorial of", num, "is", result)

# List mutability example
def modify_list(my_list):
    my_list.append(4)
    my_list[1] = 100

# Creating a list
numbers = [1, 2, 3]
print("Original List:", numbers)

# Modifying the list
modify_list(numbers)
print("Modified List:", numbers)
