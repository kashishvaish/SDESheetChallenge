from os import *
from sys import *
from collections import *
from math import *


def rotateMatrix(mat, n, m):
    # Time: O(n)  Space: O(n)
    row_start = 0
    row_end = n-1
    col_start = 0
    col_end = m-1
    while row_start < row_end and col_start < col_end:
        elements = []
        for col in range(col_start, col_end+1):
            elements.append(mat[row_start][col])
        for row in range(row_start+1, row_end):
            elements.append(mat[row][col_end])
        for col in range(col_end, col_start-1, -1):
            elements.append(mat[row_end][col])
        for row in range(row_end-1, row_start, -1):
            elements.append(mat[row][col_start])
            
        elements = [elements[-1]] + elements[:-1]
        i = 0
        
        for col in range(col_start, col_end+1):
            mat[row_start][col] = elements[i]
            i += 1
        for row in range(row_start+1, row_end):
            mat[row][col_end] = elements[i]
            i += 1
        for col in range(col_end, col_start-1, -1):
            mat[row_end][col] = elements[i]
            i += 1
        for row in range(row_end-1, row_start, -1):
            mat[row][col_start] = elements[i]
            i += 1
        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -=1

            
# Approach

# Rotate layer by layer -> one layer at a time

# 1   2   3   4
# 5   6   7   8
# 9   10  11  12
# 13  14  15  16

# Outermost elements - First Layer
# 1 2 3 4 8 12 16 15 14 13 9 5
# rotate by 1
# 5 1 2 3 4 8 12 16 15 14 13 9

# Inner elements - Second Layer
# 6 7 11 10
# rotate by 1
# 10 6 7 11

# Time: O(n)
# Space: O(n)
