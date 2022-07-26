from typing import List


def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    numsDict = {}
    for num in arr:
        if num in numsDict:
            numsDict[num] += 1
        else:
            numsDict[num] = 1
    return sorted([key for key, value in sorted(numsDict.items(), key=lambda x: -x[1])[:k]])
