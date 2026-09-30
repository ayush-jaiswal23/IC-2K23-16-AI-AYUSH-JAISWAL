def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []
    
    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            traversal_order.append(current)
            
            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return traversal_order

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Iterative:", dfs_iterative(graph, 'A'))
