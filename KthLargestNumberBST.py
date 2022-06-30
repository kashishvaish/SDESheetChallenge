'''

    ------- Binary Tree node structure --------
            class TreeNode :
                def __init__(self, data):
                    self.data = data
                    self.left = None
                    self.right = None
                    
                def __del__(self):
                    if self.left:
                        del self.left
                    if self.right:
                        del self.right
                        
'''

def KthLargestNumber(root, k):
    # Time: O(n)  Space: O(n) --> for Recursion Stack
    count = [1]
    result = [-1]
    kthLargestUtil(root, k, count, result)
    return result[0]

def kthLargestUtil(node, k, count, result):
    if not node:
        return
    kthLargestUtil(node.right, k, count, result)
#     print("Count -> ", count[0], "\nValue -> ", node.data, "\n\n")
    if count[0] == k:
        result[0] = node.data
        count[0] += 1
        return
    
    count[0] += 1
    kthLargestUtil(node.left, k, count, result)
    
# Approach
# Reverse Inorder traversal -> return kth node
# 1. Traverse Right Subtree
# 2. Traverse Current Node
# 3. Traverse Left Subtree
# Time: O(n)
# Space: O(n) --> for Recursion Stack
