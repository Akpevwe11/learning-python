"""
This method uses the divide and conquer approach to solving the problem:

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

"""


import  collections

def longestSubstring_divide_conquer(s: str, k: int) -> int:
    """
    Finds the length of the longest substring where each character's frequency >= k.
    Uses a divide and conquer approach.

    :param s:
    :param k:
    :return:

    """

    n = len(s)
    if n == 0 or n < k:
        return 0
    if k <= 1: # If k is 1 or less, any non-empty substring is valid
        return n

    # Calculate frequency of characters in the current string s
    counts = collections.Counter(s)

    # Find the first character with frequency < k to use as a split point
    split_char = None
    for i in range(n):
        if counts[s[i]] < k:
            split_char = s[i]
            break

    # If no character has frequency < k, The whole string is valid
    if split_char is None:
        return n