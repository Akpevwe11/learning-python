"""
link: https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=binary-search

problem: Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
"""


from typing import List


def minSubArrayLen(target: int, nums: List[int]):
    left = 0
    total = 0
    min_len = float('inf')

    for right in range(len(nums)):
        total += nums[right]

        while total >=target:
            min_len = min(min_len, right - left + 1)
            total-= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

