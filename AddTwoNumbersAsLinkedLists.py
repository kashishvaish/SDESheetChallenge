from os import *
from sys import *
from collections import *
from math import *

# List Node Class.
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next


def addTwoNumbers(head1, head2):
    # Time: O(m+n)  Space: O(1)
    if not head1:
        return head2
    if not head2:
        return head1
    head = Node(0)
    tail = head
    carry = 0
    p1 = head1
    p2 = head2
    while p1 and p2:
        sum = p1.data + p2.data + carry
        tail.next = Node(sum%10)
        carry = sum//10
        tail = tail.next
        p1 = p1.next
        p2 = p2.next
    while p1:
        sum = p1.data + carry
        tail.next = Node(sum%10)
        carry = sum//10
        tail = tail.next
        p1 = p1.next
    while p2:
        sum = p2.data + carry
        tail.next = Node(sum%10)
        carry = sum//10
        tail = tail.next
        p2 = p2.next
    if carry:
        tail.next = Node(carry)
    return head.next

# Approach

# Iterate through the two linked lists -> add the values and keep track of carry
# Time: O(m+n)
# Space: O(1)
