def areAnagram(str1, str2):
    # Time: O(m+n)  Space: O(m+n)
    hash1 = {}
    hash2 = {}
    for ch in str1:
        if ch not in hash1:
            hash1[ch] = 1
        else:
            hash1[ch] += 1
    for ch in str2:
        if ch not in hash2:
            hash2[ch] = 1
        else:
            hash2[ch] += 1
    if len(hash1) != len(hash2):
        return False
    for ch in hash1:
        if ch not in hash2:
            return False
        elif hash1[ch] != hash2[ch]:
            return False
    return True

# Sort and compare
# Time: O(mlogm + nlogn)
# Space: O(1)

# Hashing
# Count freq of characters in both string -> if frequencies are equal -> They are anagrams
# Time: O(m+n)
# Space: O(m+n)
