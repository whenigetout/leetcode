# Problem: 3. Longest Substring Without Repeating Characters
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: O (n^2) worst case
# Space Complexity: O (k) where k is the chars tracked in set
# Notes: This is NOT optimal. It's not truly sliding window cause it
#   restarts the work everytime it encounters a duplicate. A proper version 
#   is in solution2, where it shrinks the window without restarting everything

from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l = 0
        r = 0
        longest = 0
        cur_len = 0
        found = set()
        while r < len(s):
            if s[r] not in found:
                found.add(s[r])
                cur_len += 1
                longest = max(longest, cur_len)
                r += 1
            else:
                l += 1
                found.clear()
                r = l
                cur_len = 0
        return longest