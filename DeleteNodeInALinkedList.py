from os import *
from sys import *
from collections import *
from math import *

# Following is the List Node Class
class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(node):
    # Time: O(n)  Space: O(1)
    curr = node
    prev = None
    while curr.next:
        prev = curr
        curr.data = curr.next.data
        curr = curr.next
    prev.next = None
    
# Approach

# To delete a node -> we can shift data of nodes to left node and remove last node
# Example:
# 1->2->3->4
# To Delete 2
# Copy value 3 to left node
# 1->3->3->4
# Copy value 4 to left node
# 1->3->4->4
# Remove last node
# 1->3->4

# Time: O(n)
# Space: O(1)
