# Problem: 100. Same Tree
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        que = deque()
        que.append((p, q))

        while que:
            pair = que.popleft()
            t1, t2 = pair
            # if one of them is a node but the other is not
            if (t1 is None) != (t2 is None):
                return False
            if t1 and t2:
                if t1.val != t2.val:
                    return False
            
                que.append((t1.left, t2.left))
                que.append((t1.right, t2.right))

        return True