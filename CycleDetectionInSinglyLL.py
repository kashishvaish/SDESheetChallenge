from os import *
from sys import *
from collections import *
from math import *

'''
    class Node :
        def __init__(self, data) :
            self.data = data
            self.next = None
'''

def detectCycle(head) :
    # Time: O(n) Space: O(1)
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    
# Approach

# Using Hashing

# Traverse through the linked list
# Keep storing traversed nodes in a set
# if a node is encountered which is already in the set
# It means cycle exist

# Time: O(n)
# Space: O(n)

# Using Floyd's Cycle Detection Algorithm

# Keep two pointers fast and slow, both initially pointing at the head of the linked list
# while the end is not reached
# Keep updating fast by 2 steps and slow by 1 step
# if at any point they both point at same node -> cycle exist
# if end is reached -> cycle do not exist

# why does this algorithm work?

# Consider a circular track
# If two people A and B started moving on the track
# Speed of A is x
# Speed of B is 2x

# After 1 min -> A covers 0.25 and B covers 0.5
# After 2 min -> A covers 0.5 and B covers 1 complete round
# After 3 min -> A covers 0.75 and B covers 1.5 
# After 4 min -> A covers 1 and B covers 2 complete rounds
# Hence, they are bound to meet at a point as a cycle exist

# Time: O(n)
# Space: O(1)
