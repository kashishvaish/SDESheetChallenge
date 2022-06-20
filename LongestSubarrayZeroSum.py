from os import *
from sys import *
from collections import *
from math import *

def LongestSubsetWithZeroSum(arr):
    sumDict = {0: -1}
    currSum = 0
    maxLen = 0
    for i, num in enumerate(arr):
        currSum += num
        if currSum in sumDict:
            maxLen = max(maxLen, i-sumDict[currSum])
        else:
            sumDict[currSum] = i
    return maxLen

# Brute Force
# For every subarray -> calculate its sum -> return length of longest subarray with 0 sum
# Time: O(n^3)
# Space: O(1)

# Optimized Brute Force
# Calculated sum in the same loop used to create subarrays
# Time: O(n^2)
# Space: O(1)

# Using Hashing
# Keep track of sum upto given index
# If that sum = 0 or that sum has appeared earlier -> it marks the ending of a 0 sum subarray at that point
# Time: O(n)
# Space: O(n)
