from sys import stdin

def nextGreater(arr,n):
    # Time: O(n)  Space: O(n)
    stack = []
    result = [-1]*n
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            ind = stack.pop()
            result[ind] = arr[i]
        stack.append(i)
    return result

# Brute Force
# For every element -> traverse the right subarray and note the first number found greater than the element in result array
# Time: O(n^2)
# Space: O(1)

# Using Stack
# Initialize an empty stack
# Initialize a result array of size n with all values equal to -1
# Traverse through the array
# for element at index i -> while stack is not empty and array element at index at top of stack is less than the element -> pop from stack and do result[popped index] = arr[i] -> push index in stack
# Time: O(n)
# Space: O(n)
    
    
    
    
    
      
#Main

t = int(stdin.readline().rstrip())

while t>0:
    
    n=int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    z=(nextGreater(arr,n))
    for i in z:
        print(i,end=" ")
    print()
    
    t -= 1
