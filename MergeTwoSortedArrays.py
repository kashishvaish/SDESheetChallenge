from os import *
from sys import *
from collections import *
from math import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    p1 = m-1
    p2 = n-1
    i = m+n-1
    while p1 >= 0 and p2 >= 0:
        if arr1[p1] > arr2[p2]:
            arr1[i] = arr1[p1]
            p1 -= 1
        else:
            arr1[i] = arr2[p2]
            p2 -= 1
        i -= 1
    while p2 >= 0:
        arr1[i] = arr2[p2]
        p2 -= 1
        i -= 1
    return arr1

# Approach

# Merge both array and sort
# Time: O((n+m)log(n+m))
# Space: O(1)


# Using Three Pointers 
# start comparing both array elements from ends
# keep on inserting the greater one at last empty position
# Time: O(n+m)
# Space: O(1)
