def maximumMeetings(start, end):
    # Time: O(nlogn)  Space: O(1)
    n = len(start)
    result = []
    meetings = list(zip([x for x in range(1, n+1)], start, end))
    meetings.sort(key = lambda x: x[2])
    time = -1
    for ind, start, end in meetings:
        if time < start:
            result.append(ind)
            time = end
    return result
    
    
# Approach

# Greedy Method
# Sort meetings with respect to end times
# Select 1st meeting
# Keep on selecting meetings whose start time is lesser than current meeting's end time

# Time: O(nlogn)
# Space: O(1)
