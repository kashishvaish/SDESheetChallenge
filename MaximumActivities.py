def maximumActivities(start, finish):
    # Time: O(nlogn)  Space: O(n) --> for storing intervals
    intervals = list(zip(start, finish))
    intervals.sort(key = lambda x: x[1])
    time = 0
    count = 0
    for st, et in intervals:
        if st >= time:
            count += 1
            time = et
    return count
            
# Approach
# Greedy Algorithm

# Greedy Choice --> Select the activity whose end time is least among the remaining activities and start time is start time is more than or equal to the end time of the previously selected activity. 
# For this:
# 1. Sort intervals based on end time
# 2. Select the first interval
# 3. Keep on selecting intervals whose start time is greater than the end time of the previously selected interval.

# Time: O(nlogn)
# Space: O(n) --> for storing intervals
