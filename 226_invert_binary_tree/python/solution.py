# Problem: 226. Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(root: Optional[TreeNode]):
            if not root:
                return
            recur(root.left)
            recur(root.right)
            
            # invert
            tmp = root.right
            root.right = root.left
            root.left = tmp

        recur(root)
        return root