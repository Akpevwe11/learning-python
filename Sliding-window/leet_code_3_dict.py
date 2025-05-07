def length_of_longest_substring(s: str) -> int:
    char_index_map = {}  # stores character and its last seen index
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1  # move left past the last occurrence
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3