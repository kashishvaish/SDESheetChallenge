def distinctSubstring(word):
    subs = set()
    n = len(word)
    for i in range(n):
        for j in range(i+1, n+1):
            sub = word[i: j]
            subs.add(sub)
    return len(subs)
