# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLeftView(root)->list:
    # Time: O(n)  Space: O(n) --> for Recursion Stack
    traversal = []
    leftView(root, traversal, 1)
    return traversal

def leftView(node, traversal, height):
    if not node:
        return
    if len(traversal) < height:
        traversal.append(node.data)
    leftView(node.left, traversal, height+1)
    leftView(node.right, traversal, height+1)    
    
# Approach

# To check whether the node will be there in left view -> 
# Traverse tree such that left child is traversed before right child
# Keeping track of the level at which the node is present ->
# First node to be traversed of a particular level will be added in the left view

# Time: O(n)
# Space: O(n) for Recursion Stack
