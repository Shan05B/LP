import heapq 
def dijkstra(graph, start): 
    dist = {node: float('inf') for node in graph} 
    dist[start] = 0 
    pq = [(0, start)] 
    while pq: 
        current_dist, node = heapq.heappop(pq) 
        for neighbor, weight in graph[node]: 
            distance = current_dist + weight 
            if distance < dist[neighbor]: 
                dist[neighbor] = distance 
                heapq.heappush(pq, (distance, neighbor)) 
    return dist 
graph = { 
    'A': [('B', 2), ('C', 1)], 
    'B': [('A', 2), ('D', 4), ('E', 2)], 
    'C': [('A', 1), ('F', 2)], 
    'D': [('B', 4)], 
    'E': [('B', 2), ('F', 3)], 
    'F': [('C', 2), ('E', 3)] 
} 
start = 'A' 
result = dijkstra(graph, start) 
print("Shortest distances from", start) 
for node in result: 
    print(node, ":", result[node])
