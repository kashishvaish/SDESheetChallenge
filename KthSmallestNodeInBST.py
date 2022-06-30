'''
    Following is the TreeNode class structure
   
    class   TreeNode :
        def __init__(self, data) :
            self.data = data
            self.left = None
            self.right = None

        def __del__(self):
            if self.left:
                del self.left
            if self.right:
                del self.right

'''
def kthSmallest(root, k):
    # Time: O(n)  Space: O(n) --> for Recursion Stack
    count = [1]
    result = [None]
    kthSmallestUtil(root, k, count, result)
    return result[0]

def kthSmallestUtil(node, k, count, result):
    if not node:
        return
    kthSmallestUtil(node.left, k, count, result)
#     print("Count -> ", count[0], "\nValue -> ", node.data, "\n\n")
    if count[0] == k:
        result[0] = node.data
        count[0] += 1
        return
    
    count[0] += 1
    kthSmallestUtil(node.right, k, count, result)

# Approach
# Inorder traversal -> return kth node
# Time: O(n)
# Space: O(n) --> for Recursion Stack
