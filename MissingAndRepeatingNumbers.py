from os import *
from sys import *
from collections import *
from math import *

def missingAndRepeating(arr, n):
    # Time: O(n)  Space: O(1)
    for i in range(n):
        if arr[abs(arr[i])-1] < 0:
            repeated = abs(arr[i])
        else:
            arr[abs(arr[i])-1] *= -1
    for i in range(n):
        if arr[i] > 0:
            return i+1, repeated
            

# Approach

# Traverse through the array
# For every element i -> make number at index i-1 negative to mark the occurence of the element.
# If an element has already been occured -> return it as repeated element.
# If number at any index i is positive -> return i+1 as missing element.

# Time: O(n)
# Space: O(1)
