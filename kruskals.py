edges = [(1, "A", "B"), (2, "B", "C"), (3, "A", "C"), (4, "B", "D")]

parent = {}


def find(node):
    if parent[node] == node:
        return node
    return find(parent[node])


def kruskal():
    cost = 0
    vertices = ["A", "B", "C", "D"]

    for v in vertices:
        parent[v] = v

    edges.sort()
    print("Edges in MST: ")

    for w, u, v in edges:
        if find(u) != find(v):
            parent[find(u)] = find(v)
            print(u, "-", v, "=", w)
            cost += w

    print("Minimum Cost :", cost)


kruskal()
