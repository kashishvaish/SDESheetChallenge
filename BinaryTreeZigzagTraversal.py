# BinaryTreeNode class definition
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#

def zigZagTraversal(root):
    # Time: O(n)  Space: O(n)
    traversal = []
    if not root:
        return []
    curr = []
    next = []
    left = True
    curr.append(root)
    while curr:
        node = curr.pop()
        traversal.append(node.data)
        if left:
            if node.left: next.append(node.left)
            if node.right: next.append(node.right)
        else:
            if node.right: next.append(node.right)
            if node.left: next.append(node.left)
        if not curr:
            left = not left
            curr = next
            next = []
    return traversal
