from os import *
from sys import *
from collections import *
from math import *

def uniquePaths(m, n):
    # Time: O(mn)  Space: O(mn)
    dp = [[0]*n for i in range(m)]
    dp[0][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(m):
        dp[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

# Recursion 

# given matrix of dimension m x n
# if m == 1
# [start, _, _, _, ...., _, destination]
# no matter what the value of n is there will be only one way to reach the destination
# similarly, if n == 1
# [[start]
#  []
#  []
#  ..
#  []
#  [destination]]
# no matter what the value of m is there will be only one way to reach the destination
# therefore base condition for recursion --> if n == 1 or m == 1 --> paths = 1
# else -> paths = paths(m-1, n) + paths(m, n-1) --> as we can either go down or go right from a cell

# Code:
# def uniquePaths(m, n):
#     if m == 1:
#         return 1
#     if n == 1:
#         return 1
#     return uniquePaths(m-1, n) + uniquePaths(m, n-1)

# Time: O(2^(mn))
# Space: Recursion Stack Space

# Dynamic Programming
# Store values of number of ways for cells and use it to calculate number of ways for other cells

# Time: O(mn)
# Space: O(mn)
