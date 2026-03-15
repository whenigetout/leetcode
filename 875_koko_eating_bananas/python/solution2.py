# Problem: 875. Koko Eating Bananas
# URL: 
# Difficulty: Unknown
# Tags: 

from typing import List, Optional
import math

def satisfied(arr: List[int], h: int, k: int) -> bool:
    return sum([math.ceil(x / k) for x in arr]) <= h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2

            if satisfied(piles, h, mid):
                r = mid
            else:
                l = mid + 1
        
        return l
