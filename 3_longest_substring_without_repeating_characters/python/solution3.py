# Problem: 3. Longest Substring Without Repeating Characters
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: O (n) 
# Space Complexity: O (k) where k is the chars tracked in set
# Notes: The CORRECT sliding window version

from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
                
        return longest