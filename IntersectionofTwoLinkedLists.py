from os import *
from sys import *
from collections import *
from math import *


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findIntersection(firstHead, secondHead) :
    # Time: O(m+n)  Space: O(1)
    p1 = firstHead
    p2 = secondHead
    m = 0
    n = 0
    while p1:
        m += 1
        p1 = p1.next
    while p2:
        n += 1
        p2 = p2.next
    p1 = firstHead
    p2 = secondHead
    if m > n:
        for i in range(m-n):
            p1 = p1.next
    else:
        for i in range(n-m):
            p2 = p2.next
    while p1 and p2:
        if p1 == p2:
            return p1.data
        p1 = p1.next
        p2 = p2.next
    return -1  

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1
    return head


def attach(head1 , head2) :
	temp1 = head1  

	while(temp1!= None and temp1.next != None) :
		temp1 = temp1.next  
	
	temp2 = head2  
	prev = None 
	
	
	while(temp2.next != None) :
		prev = temp2  
		temp2 = temp2.next  
	
	if(prev == None) :
		if(temp1.data == head2.data) :
			temp1.next = head2  
	
	else :
		if(temp2.data == temp1.data) :
			prev.next = temp1  
	
#main

head1 = takeInput()
head2 = takeInput()
head3 = takeInput()

attach(head1, head2)
#Create Intersection
temp1 = head1  
while(temp1.next != None) :
	temp1 = temp1.next  

temp1.next = head3  

ans = findIntersection(head1, head2)  

print(ans)


# Approach

# Hashing
# Store all nodes of first linked list in a hashSet
# Traverse second linked list -> the first node that is present in hashSet is the point of intersection

# Time: O(m+n)
# Space: O(m+n)


# Calculate lengths of linked lists
# let length of LL1 = m
# let length of LL2 = n
# initialize p1 = head1 and p2 = head2
# if m > n -> move p1 forward m-n steps
# else -> move p2 forward n-m steps
# now till p1 and p2 -> 
#    check if they point to same node -> if yes return node.data
#    if not move both the pointers p1 and p2 forward by one step
# return -1

# Time: O(m+n)
# Space: O(1)
