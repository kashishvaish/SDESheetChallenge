from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    # Time: O(nm) Space: O(1)
    rows = len(matrix)
    cols = len(matrix[0])
    flag0col = 1
    
    # for first col
    for i in range(rows):
        if matrix[i][0] == 0:
            flag0col = 0
            break
            
    # for first row
    for i in range(cols):
        if matrix[0][i] == 0:
            matrix[0][0] = 0
            break
            
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    if matrix[0][0] == 0:
        for i in range(cols):
            matrix[0][i] = 0
            
    if flag0col == 0:
        for i in range(rows):
            matrix[i][0] = 0
            
    

    
# Problem Statement
# Given an ‘N’ x ‘M’ integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix. In particular, your task is to modify it in such a way that if a cell has a value 0 (matrix[i][j] == 0), then all the cells of the ith row and jth column should be changed to 0.
# You must do it in place.

# Example:
# If the given grid is this:
# [7, 19, 3]
# [4, 21, 0]

# Then the modified grid will be:
# [7, 19, 0]
# [0, 0,  0]


# Approach 1:
# By keeping the indices of row and col to be made 0 in set

# initialize two empty sets rows and cols
# iterate through the matrix,
# if matrix[i][j] == 0:
#    add i in rows set
#    add j in cols set
# for each row in row set -> make entire row 0
# for each col in col set -> make entire col 0

# Time: O(nm)
# Space: O(n+m)


# Approach 2:
# Optimizing space complexity

# instead of using separate set to mark the rows and cols, use the first element of row/col as a flag

# but here, first row first cell is also first col first cell,
# Therefore, we'll need additional flag for either of the two case.

# Time: O(nm)
# Space: O(1)
