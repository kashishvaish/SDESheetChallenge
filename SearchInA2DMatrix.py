from os import *
from sys import *
from collections import *
from math import *

def findTargetInMatrix(mat, m, n, target):
    # Time: O(m+n)  Space: O(1)
    row = -1
    for i in range(m):
        if mat[i][0] > target:
            row = i-1
            break
    for j in mat[row]:
        if j == target:
            return True
    return False

# Approach:
# Find the first row with value at 0th index greater than target
# Find target value in that row --> if found, return True --> else, return False
# Time: O(m+n)
# Space: O(1)
