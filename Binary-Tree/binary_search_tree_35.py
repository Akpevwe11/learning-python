from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    """
    This function searches for the target in the sorted list nums.
    If found, it returns the index of the target.
    If not found, it returns the index where the target can be inserted
    to maintain sorted order.
    """

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


class Solution:
    pass


