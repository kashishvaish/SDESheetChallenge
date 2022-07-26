def maximumValue(items, n, w):
    items.sort(key=lambda x: (x[1]/x[0]), reverse = True)
    curr = 0
    val = 0
    for i in range(n):
        if curr + items[i][0] <= w:
            val += items[i][1]
            curr += items[i][0]
        else:
            val += items[i][1]*(w-curr)/items[i][0]
            break
    return val
