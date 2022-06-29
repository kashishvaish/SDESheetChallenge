def reverseString(str):
    # Time: O(n)  Space: O(n)
    words = [word for word in str.split() if len(word) != 0]
    return " ".join(words[::-1])
    
# Approach

# 1. Split string accross spaces into a list of strings.
# 2. Remove empty strings from list. Ex -> "Hi  " -> ["Hi", ""] --> Therefore we need to remove such empty strings
# 3. Reverse the list of strings.
# 4. Join them into a string with each individual word separated by space.

# Time: O(n)
# Space: O(n)
