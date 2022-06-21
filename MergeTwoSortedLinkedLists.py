from os import *
from sys import *
from collections import *
from math import *

import sys
from sys import stdin

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def sortTwoLists(first, second):
    # Time: O(m+n) Space: O(1)
    if not first:
        return second
    if not second:
        return first
    if first.data < second.data:
        head = first
        last = first
        first = first.next
    else:
        head = second
        last = second
        second = second.next
    while first and second:
        if first.data < second.data:
            last.next = first
            last = first
            first = first.next
        else:
            last.next = second
            last = second
            second = second.next
    if first:
        last.next = first
    if second:
        last.next = second
    return head


def ll(arr):
    
    if len(arr)==0:
        return None
    
    head = Node(arr[0])
    last = head
    
    for data in arr[1:]:
        
        last.next = Node(data)
        last = last.next
        
    return head

def printll(head):
    
    while head:
        
        print(head.data, end=' ')
        
        head = head.next
        
    print(-1)

    

t = int(sys.stdin.readline().strip())

for i in range(t):
    
    arr1=list(map(int, sys.stdin.readline().strip().split(" ")))
    arr2=list(map(int, sys.stdin.readline().strip().split(" ")))
    
    l1 = ll(arr1[:-1])
    l2 = ll(arr2[:-1])
    
    l = sortTwoLists(l1, l2)
    
    printll(l)

# Approach

# Take two pointers -> both initially pointing towards the heads of the two linked lists
# compare their values -> make the node with smaller value head of the merged linked list and move that pointer forward
# keep on comparing values of nodes at those pointers -> and append the node with lower value to the end of the merged linked list
# Time: O(m+n)
# Space: O(1)
