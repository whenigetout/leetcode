# Problem: 567. Permutation In String
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        res = False
        count = Counter(s1)
        count2 = {}
        cur_len = 0
        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            cur_len += 1
            while count2[s2[r]] > count[s2[r]]:
                count2[s2[l]] -= 1
                cur_len -= 1
                l += 1
            if cur_len == len(s1):
                return True
        return res