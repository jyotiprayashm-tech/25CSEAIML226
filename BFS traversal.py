from collections import deque
def bfs(graph,start):
    visited = set()
    queue = deque()
    visited.add(start)
    queue.append(start)
    print("BFS traversal: ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
graph={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': []
}
bfs(graph,'A')