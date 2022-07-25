from os import *
from sys import *
from collections import *
from math import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Time: O(n)  Space: O(n)
    result = 0
    numsSet = set(arr)
    for num in numsSet:
        if num-1 not in numsSet:
            currNum = num
            streak = 1
            while currNum+1 in numsSet:
                streak += 1
                currNum += 1
            result = max(result, streak)
    return result
