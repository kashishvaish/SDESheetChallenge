def isValidParenthesis(expression):
    # Time: O(n)  Space: O(n)
    stack = []
    for ch in expression:
        if ch in "{([":
            stack.append(ch)
        elif ch == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif ch == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif ch == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
    if not stack:
        return True
    return False


# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")

# Using Stack
# Initialize an empty stack
# For every character in expression
#     if it is an opening bracket -> push it into stack
#     else if it is a closing bracket -> 
#         if top of stack if corresponding opening bracket -> pop from stack
#         else -> return False
# if stack is empty -> return True
# else -> return False

# Time: O(n)
# Space: O(n)
