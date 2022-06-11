from os import *
from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    for num in arr:
        if arr[abs(num)] < 0:
            return abs(num)
        arr[abs(num)] *= -1

# For each number between [1, n-1]
# Count occurence -> if > 1 -> return number

# Time: O(n^2)
# Space: O(1)

# Optimization
# Here we know that values lie between the range [1, n-1]
# We can traverse through the array,
# for each value -> make value at that index negative to mark that the element has been visited
# if an element will be repeated, we will see that the value at that index is already negative
# Therefore, return that element

# Time: O(n)
# Space: O(1)
