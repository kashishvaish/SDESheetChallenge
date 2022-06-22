def longestPalinSubstring(str):
    # Time: O(n^2)  Space: O(n^2)
    n = len(str)
    if n == 0:
        return ""
    dp = [[False]*n for i in range(n)]
    maxLen = 1
    start = 0
    for i in range(n):
        dp[i][i] = True
        if i < n-1 and str[i] == str[i+1]:
            dp[i][i+1] = True
            if maxLen < 2:
                maxLen = 2
                start = i
    for l in range(2, n):
        for i in range(n-l):
            if str[i]==str[i+l] and dp[i+1][i+l-1]:
                dp[i][i+l] = True
                if maxLen < l+1:
                    maxLen = l+1
                    start = i
    return str[start:start+maxLen]

# Brute Force
# For every substring -> check whether it is palindrome or not -> return length of longest palindromic substring
# Time: O(n^3)
# Space: O(1)

# Dynamic Programming
# Observation:
# 1. Substring of length 1 -> always palindrome
# 2. Substring of length 2 -> palindrome if both characters are equal
# 3. Else -> if substring excluding first and last character is palindrome then that substring is palindrome
# Time: O(n^2)
# Space: O(n^2)
