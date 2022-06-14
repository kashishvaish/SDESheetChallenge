from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    buy = 0
    sell = 1
    maxProfit = 0
    while sell < len(prices):
        maxProfit = max(maxProfit, prices[sell]-prices[buy])
        if prices[sell] < prices[buy]:
            buy = sell
        sell += 1
    return maxProfit
    
# Best Time to Buy and Sell Stock
# Condition -> can buy and sell only once

# Brute Force
# For all possible ways -> calculate profit -> return max profit

# Time: O(n^2)
# Space: O(1)

# Optimized Approach
# Two pointers

# Take two pointers buy and sell
# Initially buy = 0 and sell = 1
# Initialize maxProfit = 0
# while sell < len(prices) do
#    maxProfit = max of maxProfit or prices[sell]-prices[buy]
#    if sell price is less than buy price it means we should buy at that price so do 
#        buy = sell
#    sell += 1
# return maxProfit

# Time: O(n)
# Space: O(1)
