def jobScheduling(jobs):
    # Time: O(nlogn) + O(n x m)  Space: O(m)
    jobs.sort(key = lambda x: x[1], reverse = True)
    maxDeadline = max([x[0] for x in jobs])
    arr = [-1]*(maxDeadline+1)
    profit = 0
    for job in jobs:
        for time in range(job[0], 0, -1):
            if arr[time] == -1:
                arr[time] = 1
                profit += job[1]
                break
    return profit 
