from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    maxCurr = 0
    maxTillNow = 0 # if you want to consider negative sum as well -> initialize maxTillNow by -infinity i.e. float('-inf') 
    for i in range(n):
        maxCurr += arr[i]
        maxTillNow = max(maxTillNow, maxCurr)
        if maxCurr < 0:
            maxCurr = 0
    return maxTillNow

# Approach

# Brute Force

# For all subarrays calculate sum of subarray
# return the maximum sum
# Time: O(n^3)
# Space: O(1)

# Optimized Brute Force

# Calculate sum in same loop
# Time: O(n^2)
# Space: O(1)


# Kadane's Algorithm

# Keep track of two sums
# 1) Current max sum
# 2) Max sum till now
# MaxTillNow will contain the max sum of subarray

# Intuition: 
# Look for all positive contiguous segments of the array.
# Keep track of maximum sum contiguous segment among all positive segments. 
# Each time we get a positive sum compare it with max till now and update max till now if it is greater than max till now.

# Time: O(n)
# Space: O(1)









#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
