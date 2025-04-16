
def find_unique_element(arr):
    unique = 0
    for num in arr:
        unique ^= num
    return unique

# Example usage
if __name__ == "__main__":
    arr = [4, 1, 2, 1, 2]
    print(find_unique_element(arr))  # Output: 4
