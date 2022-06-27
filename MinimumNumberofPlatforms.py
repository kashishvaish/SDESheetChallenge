from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(at, dt, n):
    # Time: O(nlogn)  Space: O(n)
    slots = [[1, at[i]] for i in range(n)] + [[-1, dt[i]] for i in range(n)]
    slots.sort(key = lambda x: (x[1], -x[0]))
    result = 0
    count = 0
    for i, j in slots:
        if i == 1:
            count += 1
            result = max(result, count)
        else:
            count -= 1
    return result
            

# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)
    
# Approach

# To find minimum number of platforms --> find maximum number of trains with their intervals overlapping each other --> i.e. maximum number of trains at platform at any point of time

# For this denote flag 1 as arrival of train 
# denote flag -1 as departure of train
# combine arrival and departure time values with their flags values in a single array and sort them first with respect to time first and then in decreasing order of arrival time
# then traverse through the array keeping track of the number of trains currently at the platforms --> return max number of trains that are present at a time.

# Time: O(nlogn)
# Space: O(n)
