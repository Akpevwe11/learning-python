"""
Problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem: Search in Rotated Sorted Array

Given an integer array nums sorted in ascending order, and an integer target,
find the index of target in nums. If target is not in nums, return -1.
If nums was originally sorted in ascending order, then rotated at some pivot
unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    """
    This function searches for the target in the rotated sorted array nums.
    If found, it returns the index of the target.
    If not found, it returns -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            # Target is in the left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            # Target is in the right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1  # Target not found




