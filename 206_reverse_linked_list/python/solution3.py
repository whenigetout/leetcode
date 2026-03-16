# Problem: 206. Reverse Linked List
# URL: 
# Difficulty: Unknown
# Tags: 

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def recur(head: Optional[ListNode], rest: Optional[ListNode]):
    if not rest:
        return head
    
    nxt = rest.next
    rest.next = head

    return recur(rest, nxt)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return recur(None, head)