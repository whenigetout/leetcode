# Problem: 235. Lowest Common Ancestor Of A Binary Search Tree
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        -since this is a bst, just check until p < current node < q
        """
        cur, x, y = root.val, p.val, q.val
        if cur == x or cur == y or x < cur < y or y < cur < x:
            return root
        if x < cur:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)