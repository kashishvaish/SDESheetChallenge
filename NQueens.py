def solveNQueens(n):
    # Time: O(N! x N)  Space: O(N^2)
    poss = []
    board = [[0]*n for i in range(n)]
    getSolutions(poss, board, 0, n)
    return poss

def getSolutions(poss, board, i, n):
    if i == n:
        ans = []
        for i in range(n):
            ans += board[i]
        poss.append(ans)
        return
    for j in range(n):
        if isSafe(board, i, j, n):
            board[i][j] = 1
            getSolutions(poss, board, i+1, n)
            board[i][j] = 0

def isSafe(board, i, j, n):
    for row in range(i):
        if board[row][j] == 1:
            return False
        if j-(i-row) >= 0 and board[row][j-(i-row)] == 1:
            return False
        if j+(i-row) < n and board[row][j+(i-row)] == 1:
            return False
    return True

# Approach

# Backtracking
# Place Queens in one row at a time to reach the solution

# Time: O(N! x N)
# Space: O(N^2)
