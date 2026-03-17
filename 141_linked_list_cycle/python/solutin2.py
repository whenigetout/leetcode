# Problem: 141. Linked List Cycle
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: O(1) space using Floyd's algorithm. have 2 pointers one 
#   slow one fast. fast moves twice as fast as the slow pointer.
#   if there's a cycle, they must eventually meet

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
            
        return False