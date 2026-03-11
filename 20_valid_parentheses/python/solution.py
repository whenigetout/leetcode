# Problem: 20. Valid Parentheses
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        res = False
        for c in s:
            if c in matching.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if opening != matching[c]:
                    return False
        if len(stack) == 0:
            res = True

        return res