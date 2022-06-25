from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

#Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
            
            
def isPalindrome(head):
    # Time: O(n)  Space: O(1)
    if not head or not head.next:
        return True
    mid = getMid(head)
    mid.next = reverse(mid.next)
    p1 = head
    p2 = mid.next
    while p2:
        if p1.data != p2.data:
            return False
        p1 = p1.next
        p2 = p2.next
    return True

def getMid(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def reverse(head):
    prev = None
    curr = head
    next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    
def takeinput():
    
    inputlist=[int(ele) for ele in input().split()]
    
    head=None
    tail=None
    
    for currentData in inputlist:
        
        if currentData == -1:
            break
        
        Newnode=Node(currentData)
        
        if head is None:
            head=Newnode
            tail=Newnode
        else:
            tail.next=Newnode
            tail=Newnode
            
    return head







#Main
t = int(stdin.readline().rstrip())

while t > 0:
    
    head = takeinput()
    
    if isPalindrome(head):
        print('true')
    else:
        print('false')
        
    t -= 1

    
# Approach

# Traverse linked list -> Store values in an array -> Check if the values are palindrome or not
# Time: O(n)
# Space: O(n)

# Reverse second half of linked list
# Compare values from one pointer initially at head and second pointer initially at mid.next to check palindrome
# Time: O(n)
# Space: O(1)
