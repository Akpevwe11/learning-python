"""
problem 219 Contains Duplicate II

Given an integer array `nums` and an integer k, return true if there are two distinct indices i and j in the array\
such that nums[i] == nums[j] and abs(i - j) <= k

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""

def containsNearbyDuplicate(nums, k):
    num_indices = {}

    for i, num in enumerate(nums):
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i
    return False