def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# User input
numbers = input("Enter a sorted list of numbers (space-separated): ").split()
numbers = [int(num) for num in numbers]

target = int(input("Enter the target value: "))

# Perform binary search
result = binary_search(numbers, target)

# Display the result
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
