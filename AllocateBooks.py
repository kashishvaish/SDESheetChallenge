def ayushGivesNinjatest(n, m, time):
    # Time: O(mlogn)  Space: O(1)
    if m == 0: return 0
    left = max(time)
    right = sum(time)
    answer = -1
    while left <= right:
        mid = (left+right) // 2
        if isPossible(n, m, time, mid):
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer

def isPossible(n, m, time, limit):
    count = 1
    currSum = 0
    for i in range(m):
        currSum += time[i]
        if currSum > limit:
            count += 1
            currSum = time[i]
    if count <= n:
        return True
    return False
            
    
# Approach
# Binary Search
# Here we know the range within which our answer will lie
# Also, if time t is valid --> then all the values greater than t will also be valid
# And if a time t is invalid --> then all the values lesser than t will also be invalid
# Hence this is a monotonic series --> and we need to find the first value of time for which all chapters can be read within n days.

# Time: O(mlogn)
# Space: O(1)
