from os import *
from sys import *
from collections import *
from math import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    # Time: O(n) Space: O(1)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Approach

# Calculate length of Linked List then return the node at half length
# Time: O(n)
# Space: O(1)

# Using Two Pointers

# Intuition:
# Consider a road of distance d
# if two people A and B, start walking from the beginning at same time
# and speed of A is x
# and speed of B is 2x
# When B reach the end i.e. travelled d distance
# at time time A would have travelled d/2 distance
# Therefore, A will be at the mid point

# Take two pointers slow and fast, both initially pointing at the head
# while fast does not reach the end
#     update slow by one step
#     update fast by two steps
# return slow

# Time: O(n)
# Space: O(1)
