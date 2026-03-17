# Problem: 104. Maximum Depth Of Binary Tree
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def max_depth(root: Optional[TreeNode]):
            if not root:
                return 0
            return 1 + max(max_depth(root.left), max_depth(root.right))
        
        return max_depth(root)