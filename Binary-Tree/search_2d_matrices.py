"""
link: https://leetcode.com/problems/search-a-2d-matrix/?envType=problem-list-v2&envId=binary-search

Problem: Search a 2D Matrix
Given an m x n matrix, return true if target is in the matrix and false otherwise.
You must write a solution in O(log(m * n)) time complexity.
Example 1:

Input: matrix = [[1,3,5],[7,9,11],[12,13,15]], target = 9

Output: true

Example 2:


"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False



# Example usage
matrix = [[1, 3, 5], [7, 9, 11], [12, 13, 15]]

target = 9
solution = Solution()
result = solution.searchMatrix(matrix, target)
print(result)  # Output: True
target = 10
result = solution.searchMatrix(matrix, target)
print(result)  # Output: False
target = 15
result = solution.searchMatrix(matrix, target)
print(result)  # Output: True