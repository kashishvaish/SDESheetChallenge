'''

    Following is the representation for the Binary Tree Node:

    class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
'''

def isSymmetric(root) :
    # Time: O(n)  Space: O(n) for Recursion Stack
    if not root:
        return True
    return isIdentical(root, root)

def isIdentical(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.data != node2.data:
        return False
    return isIdentical(node1.left, node2.right) and isIdentical(node1.right, node2.left)

# Approach
# Check whether the tree and its mirror image are identical

# Time: O(n)
# Space: O(n) for Recursion Stack
