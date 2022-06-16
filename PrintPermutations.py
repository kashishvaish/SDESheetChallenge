def findPermutations(s):
    # Time: O(n*n!)  Space: O(n!)
    permutations = []
    getPerms(s, "", permutations)
    return permutations

def getPerms(s, temp, permutations):
    if not s:
        permutations.append(temp)
        return
    for i in range(len(s)):
        getPerms(s[:i]+s[i+1:], temp+s[i], permutations)
        
# Approach
# Recursion
# Time: O(n*n!)
# Space: O(n!) 
