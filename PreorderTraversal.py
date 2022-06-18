'''
	 
	 Following is the Binary Tree node structure:
	 
	 class TreeNode:
	     def __init__(self, data=0, left=None, right=None):
	         self.data = data
	         self.left = left
	         self.right = right
'''

def getPreOrderTraversal(root):
    # Time: O(n)  Space: O(n)
    traversal = []
    preorder(root, traversal)
    return traversal

def preorder(root, traversal):
    if not root:
        return
    traversal.append(root.data)
    preorder(root.left, traversal)
    preorder(root.right, traversal)

# Preorder

# 1. Traverse node
# 2. Traverse Left Subtree
# 3. Traverse Right Subtree

# Time: O(n)
# Space: O(n) for recursion
