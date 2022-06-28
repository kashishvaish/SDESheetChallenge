# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowestCommonAncestor(root, x, y):
    # Time: O(n)  Space: O(n) --> for Recursion Stack 
    if not root:
        return None
    if root.data == x or root.data == y:
        return root.data
    l = lowestCommonAncestor(root.left, x, y)
    r = lowestCommonAncestor(root.right, x, y)
    if l != None and r != None:
        return root.data
    elif l != None:
        return l
    return r

# Approach

# If we traverse nodes level wise
# For a node -> if it is equal to either x and y -> it will be LCA
# If either of x or y lies in its left subtree and the other one lies in its right subtree --> it will be LCA
# Else -> recur to left and right subtrees

# Time: O(n)
# Space: O(n) for Recursion stack space
