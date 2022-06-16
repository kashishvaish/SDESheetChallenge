from os import *
from sys import *
from collections import *
from math import *

def findMajorityElement(arr, n):
    # Time: O(n)  Space: O(1)
    if n == 0:
        return -1
    candidate = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] == candidate:
            count += 1
        else:
            count -= 1
            if count <= 0:
                candidate = arr[i]
                count = 1
    freq = 0 
    for i in range(n):
        if arr[i] == candidate:
            freq += 1
    if freq > n//2:
        return candidate
    return -1
# Hashing

# Use hashMap to count the occurence of each element and return the majority element
# Time: O(n)
# Space: O(n)

# Keeping track of potential candidate

# Traverse through the array keeping track of the potential candidate
# Initially first element will be the potential candidate, set count = 1
# for next item, if it is equal to the potential candidate, increment count by 1
# else, decrement count by 1
# if count == 0 -> the newly found element will act as the new candidate
# at the end count frequency of the candidate -> if frequency > n / 2 --> return candidate, else return -1

# Time: O(n)
# Space: O(1)
