# Problem: 153. Find Minimum In Rotated Sorted Array
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]