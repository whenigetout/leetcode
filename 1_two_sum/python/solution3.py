from typing import List

def twoSum(nums: List[int], target: int):
    seen = {}

    for idx, val in enumerate(nums):
        if target - val in seen:
            return [idx, seen[target - val]]
        if val not in seen:
            seen[val] = idx

    # no 2 elems sum to target
    return []