# Problem: 102. Binary Tree Level Order Traversal
# URL: 
# Difficulty: Unknown
# Tags: 
# Note: 2nd run of 150

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        q = deque([root])
        while q:
            n = len(q)
            lvl = []
            for _ in range(n):
                node = q.popleft()
                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lvl)
        
        return res