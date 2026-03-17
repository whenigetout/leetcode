# Problem: 19. Remove Nth Node From End Of List
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: Better than prev version, single pass on the list

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        2 pointers, start them with a gap of 'n', and after traversal we end 
        up at the nth node from the end
        """
        dummy = ListNode()
        dummy.next = head

        p1 = dummy
        p2 = dummy
        count = n

        while count:
            p2 = p2.next
            count -= 1

        # now there's a gap of 'n' btw the pointers. traverse the list
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next

        # now p1 is right before the node to delete
        p1.next = p1.next.next
        return dummy.next
