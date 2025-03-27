from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            # Process nodes level by level
            for i in range(level_size):
                node = queue.popleft()
                # Capture the rightmost element of this level
                if i == level_size - 1:
                    result.append(node.val)
                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


# Example usage:
if __name__ == "__main__":
    # Constructing the following binary tree:
    #      1
    #     / \
    #    2   3
    #     \   \
    #      5   4
    root = TreeNode(1)
    root.left = TreeNode(2, right=TreeNode(5))
    root.right = TreeNode(3, right=TreeNode(4))

    sol = Solution()
    print(sol.rightSideView(root))  # Output: [1, 3, 4]
