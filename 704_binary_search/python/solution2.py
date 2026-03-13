# Problem: 704. Binary Search
# URL: 
# Difficulty: Unknown
# Tags: 

from typing import List, Optional

def bsearch(arr: List[int], l: int, r: int, target: int) -> int:
    if l > r:
        return -1
    
    mid = l + (r - l) // 2
    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        return bsearch(arr, l, mid - 1, target)
    else:
        return bsearch(arr, l, mid + 1, target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bsearch(nums, 0, len(nums) - 1, target)