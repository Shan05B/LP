# BFS AND DFS

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['A',],
    'D':['B'],
    'E':['B']
}

def dfs(start,goal):
    visited=[]
    stack=[start]
    
    while stack:
        node=stack.pop()
        if node not in visited:
            print(node,end=" ")
            visited.append(node)
            
            if node==goal:
                print("\nGoal Node Found!")
                return
            
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)
                    
    print("\nGoal Node Not Found! ")
    
print("DFS Traversal : ")
dfs('A','C')


def bfs(start,goal):
    visited=[]
    queue=[start]
    
    while queue:
        node=queue.pop(0)
        if node not in visited:
            print(node,end=" ")
            visited.append(node)
            
            if node==goal:
                print("\nGoal Node Found!")
                return
            
            for neighbour  in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    
    print("\nGoal Node Not Found")
    
print("\nBFA Traversal: ")
bfs('A','E')
