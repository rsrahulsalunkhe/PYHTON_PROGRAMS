def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# User input
numbers = input("Enter a list of numbers (space-separated): ").split()
numbers = [int(num) for num in numbers]

target = int(input("Enter the target value: "))

# Perform linear search
result = linear_search(numbers, target)

# Display the result
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
