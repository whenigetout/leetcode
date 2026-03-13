# Problem: 853. Car Fleet
# URL: 
# Difficulty: Unknown
# Tags: 

from typing import List, Optional

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_v = list(zip(position, speed))
        p_v = sorted(p_v)
        fleets = 0
        while p_v:
            car = p_v.pop()
            fleets += 1
            while p_v and (target - p_v[-1][0]) / (p_v[-1][1]) <= (target - car[0]) / (car[1]):
                p_v.pop()
        return fleets
