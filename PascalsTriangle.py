from os import *
from sys import *
from collections import *
from math import *

def printPascal(n:int):
    # Time: O(n^2)
    # Space: O(n^2)
    pascal = [[1]*(i+1) for i in range(n)]
    for row in range(n-1):
        for col in range(row):
            pascal[row+1][col+1] = pascal[row][col] + pascal[row][col+1]
    return pascal

  
  
# Approach

# given n 

# initialize pascal as
#[1]
#[1, 1]
#[1, 1, 1]

# for row -> (0, n-1)
#    for col -> (0, row)
#        pascal[row+1][col+1] = pascal[row][col] + pascal[row][col+1]

# Time: O(n^2)
# Space: O(n^2)
