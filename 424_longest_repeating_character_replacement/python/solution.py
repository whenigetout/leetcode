# Problem: 424. Longest Repeating Character Replacement
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: O(n)
# Space Complexity: 
# Notes: 

from typing import List, Optional

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        count = {}
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
