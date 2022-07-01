def wordBreak(arr, n, target):
    # Time: O(n^2)  Space: O(n)
    arr = set(arr)
    m = len(target)
    if m == 0:
        return True
    dp = [False]*(m+1)
    dp[0] = True
    for i in range(1, m+1):
        if not dp[i] and target[:i] in arr:
            dp[i] = True
        if dp[i]:
            if i == m:
                return True
            for j in range(i+1, m+1):
                if not dp[j] and target[i: j] in arr:
                    dp[j] = True
        if dp[m]:
            return True
    return False
   
        
# Approaches

# Recursion
# Check whether a word forms prefix of target string --> remove that prefix from target and check again till target becomes empty string.

# Code
# def wordBreak(arr, n, target):
#     status = [False]
#     canBreak(arr, n, target, status)
#     return status[0]

# def canBreak(arr, n, target, status):
#     if status[0]:
#         return
#     if target == "":
#         status[0] = True
#         return
#     for i in range(n):
#         if arr[i] == target[:len(arr[i])]:
#             canBreak(arr, n, target[len(arr[i]):], status)

# Time: O(2^n)
# Space: O(1) --> but space will be used for Recursion Stack

# Dynamic Programming

# Time: O(n^2)
# Space: O(n)
