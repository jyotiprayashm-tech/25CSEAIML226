def dfs_search(graph,node,target,visited):
    visited.add(node)
    if node == target:
        return True
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_search(graph, neighbor, target, visited):
                return True
    return False
graph={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
visited = set()
target = 'F'
if dfs_search(graph, 'A', target, visited):
    print("Target node found:", target)
else:
    print("Target node not found.")