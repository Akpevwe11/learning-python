"""
link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array?envType=problem-list-v2&envId=binary-search

Problem: Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] after some rotations.
Find the minimum element of this rotated sorted array.
You must write an algorithm that runs in O(log n) time complexity.
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Example 3:
Input: nums = [1]
Output: 1

"""

from typing import List

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        # Check if the middle element is greater than the rightmost element
        if nums[mid] > nums[right]:
            left = mid + 1  # The minimum is in the right half
        else:
            right = mid  # The minimum is in the left half or at mid

    return nums[left]  # The left pointer will point to the minimum element