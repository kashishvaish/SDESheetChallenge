from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :
    # Dutch Sort
    # Time: O(n) Space: O(1)
    low = 0
    mid = 0
    high = n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -=1
    

#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)

    
    
# Approach

# Count occurences and then update

# Traverse the list and count the number of occurences of 0, 1, and 2 respectively
# let count 0 = a
# let count 1 = b
# let count 2 = c
# make first a elements = 0
# make next b elements = 1
# remaining elements = 2

# Time: O(n)
# Space: O(1)

# One pass solution
# Dutch Sort

# take 3 pointers -> low, mid and high
# [0, low-1] -> 0
# [low, mid-1] -> 1
# [mid, high] -> unknown
# [high+1, N] -> 2

# initialize 
# low = 0
# mid = 0
# high = N-1

# while mid <= high
# if arr[mid] == 0 -> swap it to the low range, increment low and mid
# elif arr[mid] == 1 -> increment mid
# elif arr[mid] == 2 -> swap with element in high range, decrement high

# Time: O(n)
# Space: O(1)
