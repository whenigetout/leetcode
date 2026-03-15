# Problem: 74. Search A 2D Matrix
# URL: 
# Difficulty: Unknown
# Tags: 
# Note: The best/intuitive solution compared to the prev ones, this treats
#   the 2d matrix as if it were a single 1d arr and applies bsearch. 
#   for converting/collapsing a 2d matrix into a 1d arr and vice versa:
#   (2d -> 1d):
#   index = row * width + col 
#   (1d -> 2d)
#   row   = index // width
#   col   = index % width

from typing import List, Optional

def bsearch(matrix: List[List[int]], target: int, l: int, r: int) -> int:
    if l > r:
        return -1
    mid = l + (r - l) // 2

    # convert 1d arr idx to original 2d matrix
    matrix_width = len(matrix[0])
    row = mid // matrix_width
    col = mid % matrix_width

    if matrix[row][col] == target:
        return mid
    if matrix[row][col] > target:
        return bsearch(matrix, target, l, mid - 1)
    return bsearch(matrix, target, mid + 1, r)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        return bsearch(matrix, target, 0, m * n - 1) >= 0