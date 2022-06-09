from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    # Time: O(n)  Space: O(1)
    for i in range(n-2, -1, -1):
        if permutation[i] < permutation[i+1]:
            for j in range(n-1, i, -1):
                if permutation[j] > permutation[i]:
                    permutation[i], permutation[j] = permutation[j], permutation[i]
                    permutation[i+1:] = permutation[i+1:][::-1]
                    return permutation
    return permutation[::-1] 
                
  
        
    
# Approach

# Brute Force
# Generate all possible permutations
# Return smallest permutation greater than given permutation

# Time: O(n! x n)
# Space: O(n! x n)

# Code:
# def nextPermutation(permutation, n):
#     poss = []
#     getPerms(poss, permutation, n, [])
#     next = None
#     for p in poss:
#         if p > permutation:
#             if not next:
#                 next = p
#             elif next > p:
#                 next = p
#     if not next:
#         return sorted(permutation)
#     return next
    
# def getPerms(poss, permutation, n, curr):
#     if n == 0:
#         poss.append(curr)
#         return
#     for i in range(n):
#         getPerms(poss, permutation[:i]+permutation[i+1:], n-1, curr+[permutation[i]])

# Optimized Approach

# Traverse through the permutation from end
# when a number lesser than the number of at right is encountered, swap the number with next greater number to it on its right, and reverse the right part.
# if no such number exists return reversed permutation

# Time: O(n)
# Space: O(1)

# ex [2, 1, 4, 3]

# at 4
# 4 > 3 continue

# at 1
# 1 < 4
# swap 1 with next gresater number in right part i.e. 3
# [2, 3, 4, 1]
# reverse the remaining right part i.e. [4, 1]
# [2, 3, 1, 4]
