from os import *
from sys import *
from collections import *
from math import *

def getTrappedWater(arr, n) :
    # Time: O(n)  Space: O(1)
    left = 0
    right = n-1
    leftMax = 0
    rightMax = 0
    water = 0
    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] > leftMax:
                leftMax = arr[left]
            else:
                water += leftMax-arr[left]
            left += 1
        else:
            if arr[right] > rightMax:
                rightMax = arr[right]
            else:
                water += rightMax-arr[right]
            right -= 1
    return water
