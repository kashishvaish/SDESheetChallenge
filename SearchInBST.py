'''
    Following is the Binary Tree node structure:

	class BinaryTreeNode :
	    def __init__(self, data) :
	        self.data = data
	        self.left = None
	        self.right = None

'''

def searchInBST(root, x):
    # Time: O(n)  Space: O(n) for Recursion Stack
    if not root:
        return False
    if root.data == x:
        return True
    if root.data > x:
        return searchInBST(root.left, x)
    return searchInBST(root.right, x)

# Approach:
# If node data == x --> found
# If node data > x --> search in left subtree
# else --> search in right subtree

# Time: O(n)
# Space: O(n) for Recursion Stack
