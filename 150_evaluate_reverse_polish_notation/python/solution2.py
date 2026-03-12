# Problem: 150. Evaluate Reverse Polish Notation
# URL: 
# Difficulty: Unknown
# Tags: 
# Note: 2nd time after many months

from typing import List, Optional

def evalOP(x: int, y: int, op: str) -> int:
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        return int(x / y) # truncate towards zero, fk i got this wrong again
    return 0

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s not in ["+", "-", "*", "/"]:
                stack.append(int(s))
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(evalOP(x, y, s))
        return stack.pop()