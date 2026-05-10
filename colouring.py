# Simple Graph Coloring Problem

n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):

    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter number of colors: "))

color = [0] * n

# Check Safe Color
def safe(node, c):

    for i in range(n):

        if graph[node][i] == 1 and color[i] == c:
            return False

    return True

# Solve Function
def solve(node):

    if node == n:
        return True

    for c in range(1, m+1):

        if safe(node, c):

            color[node] = c

            if solve(node + 1):
                return True

            color[node] = 0

    return False

# Function Call
if solve(0):

    print("\nSolution exists. Assigned colors:\n")

    for i in range(n):

        print("Vertex", i, "---> Color", color[i])

else:
    print("No Solution")
