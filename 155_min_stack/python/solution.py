# Problem: 155. Min Stack
# URL: 
# Difficulty: Unknown
# Tags: 
# Time Complexity: 
# Space Complexity: 
# Notes: 

from typing import List, Optional

class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_stack:
            self._min_stack.append(val)
        else:
            min_val = val if val < self._min_stack[-1] else self._min_stack[-1]
            self._min_stack.append(min_val)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]