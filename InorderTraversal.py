'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''


def getInOrderTraversal(root):
    # Time: O(n)  Space: O(n)
    traversal = []
    inorder(root, traversal)
    return traversal

def inorder(root, traversal):
    if not root:
        return
    inorder(root.left, traversal)
    traversal.append(root.data)
    inorder(root.right, traversal)

# For inorder
# Traverse left subtree
# Traverse node
# Traverse right subtree

# Time: O(n)
# Space: O(n) for recursion
