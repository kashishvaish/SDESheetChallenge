from os import *
from sys import *
from collections import *
from math import *

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def removeKthNode(head, k):
    # Time: O(n)  Space: O(1)
    if not head or k == 0:
        return head
    p1 = head
    p2 = head
    for i in range(k):
        p1 = p1.next
    if not p1:
        head = head.next
        return head
    while p1.next:
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next
    return head

def build_linkedList(arr):
    head = None
    for i in range(len(arr)):
        if arr[i] == -1:
            break

        new = Node(arr[i])

        if head is None:
            head = new
            tail = new

        else:
            tail.next = new
            tail = tail.next

    return head

# Main Code.
t = int(input().strip())
for i in range(t):
    k = int(input().strip())
    arr = [int(i) for i in input().strip().split()]

    head = build_linkedList(arr)
    res_head = removeKthNode(head, k)

    while res_head is not None:
        print(res_head.data, end= " ")
        res_head = res_head.next
    print(-1)

    
# Approach

# Take two pointers p1 and p2
# Move forward pointer p1 by k steps
# if p1 == None -> remove head node and return
# while p1.next is not None,
#    move p1 and p2 by one step
# remove p2.next
# return head

# Time: O(n)
# Space: O(1)
