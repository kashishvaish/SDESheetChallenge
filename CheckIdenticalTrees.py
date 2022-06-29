# Following is the Binary Tree Node class structure
class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
              
        
def identicalTrees(root1, root2):
    # Time: O(n)  Space: O(n) for Recursion Stack
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    return identicalTrees(root1.left, root2.left) and identicalTrees(root1.right, root2.right)

# Recursion

# If curr nodes are same 
# Recur for left and right nodes

# Time: O(n)
# Space: O(n) for Recursion Stack
