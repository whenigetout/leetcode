# Problem: 230. Kth Smallest Element In A Bst
# URL: 
# Difficulty: Unknown
# Tags: 
# Note: 2nd run of 150. COULD NOT SOLVE ON MY OWN, had to check prev solutions to 
#   know the way.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None
        
        def inorder(root: Optional[TreeNode]):
            if not root:
                return

            inorder(root.left)
            self.count += 1
            if self.count == k:
                self.res = root.val
                return
            inorder(root.right)

        inorder(root)
        return self.res
            