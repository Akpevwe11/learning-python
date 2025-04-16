
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 # Find the middle index
        if arr[mid] == target:
            return mid # Target found
        elif arr[mid] < target:
            left = mid + 1 # Search in the right half
        else:
            right = mid - 1 # Search in the left half

    return -1 # Target not found

    # Example usage


arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 9))  # Output: 4


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1 # Base case: target not found

    mid = (left + right) // 2 # Find the middle index
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search_recursive(arr, 9, 0, len(arr) - 1)) # Output 4



