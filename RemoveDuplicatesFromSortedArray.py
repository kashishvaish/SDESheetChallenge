def removeDuplicates(arr,n):
    # Time: O(n)  Space: O(1)
    i = 1
    for j in range(1, n):
        if arr[j] != arr[j-1]:
            i += 1
        else:
            arr[i] = arr[j]
    return i

# Approach

# Two pointers
# Use one pointer to traverse the array
# Use another pointer to mark ending of array with unique elements

# Time: O(n)
# Space: O(1)
