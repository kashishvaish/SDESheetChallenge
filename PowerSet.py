def pwset(v):
    # Time: O(n x 2^n)  Space: O(n x 2^n) 
    poss = []
    getpowerset(v, 0, len(v), poss, [])
    return poss

def getpowerset(v, i, n, poss, temp):
    if i == n:
        poss.append(temp)
        return
    getpowerset(v, i+1, n, poss, temp+[v[i]])
    getpowerset(v, i+1, n, poss, temp)
