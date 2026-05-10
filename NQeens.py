# Simple N-Queens Problem

N = int(input("Enter Number of Queens: "))

board = [[0]*N for i in range(N)]

# Check Safe Position
def safe(r, c):

    # Row Check
    for i in range(c):

        if board[r][i] == 1:
            return False

    # Upper Diagonal
    i, j = r, c

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Lower Diagonal
    i, j = r, c

    while i < N and j >= 0:

        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True

# Solve Function
def solve(c):

    if c == N:
        return True

    for r in range(N):

        if safe(r, c):

            board[r][c] = 1

            if solve(c + 1):
                return True

            board[r][c] = 0

    return False

# Function Call
solve(0)

print("\nSolution:\n")

for row in board:
    print(row)
