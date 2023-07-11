# Binary Search Example

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

# Test data
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

# Perform binary search
result = binary_search(numbers, target)

# Display the result
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
