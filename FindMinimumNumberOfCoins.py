denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    # Greedy Approach
    # Time: O(n)  Space: O(1)
    n = len(denominations)
    i = n-1
    count = 0
    while i >= 0:
        while amount >= denominations[i]:
            amount -= denominations[i]
            count += 1
        i -= 1
    return count
    
    
# DP

# def findMinimumCoins(amount):
#     # Time: O(mn)  Space: O(n)
#     # where, m = number of denominations and n = amount
#     dp = [1000000000]*(amount+1)
#     dp[0] = 0
#     for i in range(1, amount+1):
#         for j in range(9):
#             if denominations[j] <= i:
#                 dp[i] = min(dp[i], dp[i-denominations[j]]+1)
#     return dp[-1]
