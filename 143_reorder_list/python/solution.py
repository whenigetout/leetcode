# Problem: 143. Reorder List
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle of the list
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now the middle of the list
        # detach the rest of the list and reverse it

        rest = slow.next
        slow.next = None

        # reversing the 2nd half
        prev = None
        cur = rest

        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        # prev is the new head node of the 2nd half
        # now merge the 2 lists
        l1 = head
        l2 = prev

        while l1 and l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2
            l2.next = nxt1

            l1 = nxt1
            l2 = nxt2
