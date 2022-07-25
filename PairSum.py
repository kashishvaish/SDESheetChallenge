from os import *
from sys import *
from collections import *
from math import *
from collections import defaultdict

def pairSum(arr, s):
    pairs = []
    numsDict = defaultdict(int)
    for num in arr:
        numsDict[num] += 1
    for num in numsDict:
        if s-num in numsDict:
            if num == s-num:
                pairs.extend([[num, num]]*((numsDict[num]*(numsDict[num]-1))//2))
            else:
                pairs.extend([sorted([num, s-num])]*(numsDict[num]*numsDict[s-num]))
            numsDict[num] = 0
            numsDict[s-num] = 0
            
    return sorted(pairs, key = lambda x: (x[0], x[1]))
