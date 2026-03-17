# Problem: 19. Remove Nth Node From End Of List
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: Takes 2 passes, but O(n), better version in solution2

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head: Optional[ListNode], rest: Optional[ListNode]):
    if not rest:
        return head

    nxt = rest.next
    rest.next = head
    return reverse(rest, nxt)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        reverse the list
        remove the nth node from the reversed list
        reverse the list again and return head node
        """
        reversedList = reverse(None, head)
        count = n - 1
        prev = None
        cur = reversedList

        while count:
            prev = cur
            cur = cur.next
            count -= 1

        # cur is now the nth node
        # del the cur node
        nxt = cur.next
        if prev:
            prev.next = nxt
        else:
            reversedList = nxt
        cur.next = None

        # finally reverse the list one more time and return head
        return reverse(None, reversedList)
