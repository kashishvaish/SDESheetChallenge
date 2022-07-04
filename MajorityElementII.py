from os import *
from sys import *
from collections import *
from math import *

def majorityElementII(arr):
    # Time: O(n)  Space: O(n)
    n = len(arr)
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return [key for key in count if count[key] > n//3]

# Approach

# Use hashing to keep track of frequencies --> return majority elements
# Time: O(n)
# Space: O(n)
