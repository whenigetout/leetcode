# Problem: 543. Diameter Of Binary Tree
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        for each node, the diameter = the longest path that PASSES THRU THE NODE
        which is, height of left + height of right (the len of the path is the no. of edges, not the no. of vertices)
        """
        diameter = 0
        def height(root: Optional[TreeNode]):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            nonlocal diameter
            diameter = max(diameter, left + right)

            return 1 + max(left, right)
        
        height(root)
        return diameter
