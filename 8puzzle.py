# Simple 8 Puzzle Problem

from collections import deque

goal = [[1,2,3],[4,5,6],[7,8,-1]]

def print_board(board):
    for row in board:
        print(row)
    print()

def bfs(start):

    q = deque([(start, [])])
    visited = []

    while q:

        board, path = q.popleft()

        if board in visited:
            continue

        visited.append(board)

        path = path + [board]

        if board == goal:
            print("\nSolution Found!\n")

            for step in path:
                print_board(step)
            return

        # Find blank space
        for i in range(3):
            for j in range(3):
                if board[i][j] == -1:
                    x, y = i, j

        # Possible moves
        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx, dy in moves:

            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:

                new = [row[:] for row in board]

                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]

                q.append((new, path))

# Input
print("Enter Start State (use -1 for blank):")

start = []

for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

bfs(start)
