def uniqueElement(arr, n):
    # Time: O(logn)  Space: O(1)
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if mid & 1:
            if arr[mid-1] == arr[mid]:
                start = mid+1
            elif mid+1 < n and arr[mid] == arr[mid+1]:
                end = mid-1
            else:
                return arr[mid]
        else:
            if mid-1 >= 0 and arr[mid-1] == arr[mid]:
                end = mid-2
            elif mid+1 < n and arr[mid] == arr[mid+1]:
                start = mid+2
            else:
                return arr[mid]

# Approach

# Count freq of each element -> return element with frequency 1
# Time: O(n)
# Space: O(n)

# Do the sum of unique elements in the array -> multiply it with 2 -> Subtract sum of elements of arr from it -> return answer
# i.e. return 2*(sum of unique elements) - sum of array
# Time: O(n)
# Space: O(n)

# For the first even index i -> for which value at index i+1 is not equal to value at i -> return value at i
# Time: O(n)
# Space: O(1)

# XOR of all numbers
# Duplicates will cancel each other -> therefore the result of xor of all elements will be the unique element.
# Time: O(n)
# Space: O(1)

# Binary Search
# Observation: 
# For odd index i-> if element at i-1 == element at i -> target is towards right -> else element is towards left
# For even index i -> if element at i+1 == element at i -> target is towards right -> else element is towards left
# Time: O(logn)
# Space: O(1)
