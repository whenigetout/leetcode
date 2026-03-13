# Problem: 739. Daily Temperatures
# URL: 
# Difficulty: Unknown
# Tags: 

from typing import List, Optional

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                cur_idx = stack.pop()
                res[cur_idx] = idx - cur_idx
            stack.append(idx)
        return res
