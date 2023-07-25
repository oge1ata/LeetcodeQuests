# Brute force
# time complexity O(n^2)

from typing import List
# Using hashmaps

# class Solution:
def twoSum(nums:List[int], target:int) -> List[int]:
    hashMap = {} #val:index, basically like a dictionary

    for i, n in enumerate(nums): #index and elements
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i
    return


print(twoSum([5,6,7,2], 7))