# Problem: 11. Container With Most Water
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            cur_area = w * h
            res = max(res, cur_area)

            # move the pointer
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res