def search(arr, target) :
    # Time: O(logn)  Space: O(1)
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[start] <= arr[mid]:
            if arr[start] <= target < arr[mid]:
                end = mid-1
            else:
                start = mid+1
        elif arr[mid] <= arr[end]:
            if arr[mid] < target <= arr[end]:
                start = mid+1
            else:
                end = mid-1
    return -1
