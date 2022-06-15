from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(input ) :
    # Time: O(n) Space: O(n)
    charDict = {}
    start = -1
    maxLen = 0
    for i in range(len(input)):
        if input[i] in charDict and charDict[input[i]] > start:
            start = charDict[input[i]]
        charDict[input[i]] = i
        maxLen = max(maxLen, i-start)
    return maxLen

# Approach
# Sliding window and Hashing
# Keep track of characters and the index of their last occurence

# Time: O(n)
# Space: O(n)
