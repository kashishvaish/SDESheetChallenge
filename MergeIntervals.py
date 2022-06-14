from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key = lambda x: x.start)
    stack = [intervals[0]]
    for interval in intervals[1:]:
        if interval.start <= stack[-1].end:
            stack[-1].end = max(interval.end, stack[-1].end)
        else:
            stack.append(interval)
    return stack

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)

    
# Using Stack

# First, sort intervals based on start time
# Initialize an empty stack
# Push first interval into stack
# Traverse through the remaining interval
#    if start of the interval is less than the end of the top of stack do,
#        update end of top of stack to max(end of top, end of interval)
#    else do
#        push interval into stack
# return stack 

# Time: O(nlogn + n) -> O(nlogn) for sorting
# Space: O(n)
