from os import *
from sys import *
from collections import *
from math import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    prev = None
    next = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# Reverse a linklist

# Consider a linkedlist: 
# A->B->C->D
# to reverse a linked list create an empty list
# for each node in the linked list
# insert it in the beginning of new list
# return new list

# A->B->C->D
# prev = None
# next = None
# curr = A

# next = B
# next of A = prev, A->None
# prev = curr = A
# curr = B

# next = C
# next of B = prev, B->A
# prev = curr = B
# curr = C

# next = D
# next of C = prev, C->B->A
# prev = curr = C
# curr = D

# next = None
# next of D = prev, D->C->B->A
# prev = curr = D
# curr = None

# return prev
