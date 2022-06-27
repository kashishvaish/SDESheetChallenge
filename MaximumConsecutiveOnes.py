def longestSubSeg(arr, n, k):
    # Time: O(n)  Space: O(1)
    maxLen = 0
    start = 0
    count = 0
    for end in range(n):
        if arr[end] == 0:
            count += 1
            while count > k:
                if arr[start] == 0: count -= 1
                start += 1
        maxLen = max(maxLen, end-start+1)
    return maxLen

# Brute Force
# For every substring --> Check whether it is valid or not --> return length of maximum length valid string
# Time: O(n^3) -> two loop for start and end point and one loop for calculating number of 0
# Space: O(1)

# Optimized Brute Force
# Calculate number of 0 in same loop only
# Time: O(n^2)
# Space: O(1)

# Sliding Window
# Whenever count of 0 in window exceeds k -> move start pointer towards right till a 0 is removed from the window.

# maxLen = 0
# count = 0
# start = 0
# for end = 0 to end = n-1:
#    if arr[end] == 0:
#        count += 1
#        while count > k:
#            if arr[start] == 0: count -= 1
#            start += 1
#    maxLen = max(maxLen, end-start+1)
# return maxLen

# Time: O(n)
# Space: O(1)
