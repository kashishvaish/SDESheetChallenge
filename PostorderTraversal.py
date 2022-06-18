'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''


def getPostOrderTraversal(root):
    # Time: O(n)  Space: O(n)
    traversal = []
    postorder(root, traversal)
    return traversal

def postorder(root, traversal):
    if not root:
        return
    postorder(root.left, traversal)
    postorder(root.right, traversal)
    traversal.append(root.data)

# For postorder
# Traverse left subtree
# Traverse right subtree
# Traverse node

# Time: O(n)
# Space: O(n) for recursion
