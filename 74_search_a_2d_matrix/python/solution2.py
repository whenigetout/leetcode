# Problem: 74. Search A 2D Matrix
# URL: 
# Difficulty: Unknown
# Tags: 

from typing import List, Optional

def bsearch(arr: List[int], target: int, l: int, r: int) -> int:
    if l > r:
        return -1
    mid = l + (r - l) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return bsearch(arr, target, l, mid - 1)
    else:
        return bsearch(arr, target, mid + 1, r)

def bsearchRows(matrix: List[List[int]], target: int, l: int, r: int):
    if l > r:
        return -1
    mid = l + (r - l) // 2
    if matrix[mid][0] <= target and matrix[mid][-1] >= target:
        return mid
    if matrix[mid][0] > target:
        return bsearchRows(matrix, target, l, mid - 1)
    else:
        return bsearchRows(matrix, target, mid + 1, r)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        possibleContainingRow = bsearchRows(matrix, target, 0, m - 1)
        if possibleContainingRow < 0:
            return False
        res = bsearch(matrix[possibleContainingRow], target, 0, n - 1)
        return res >= 0