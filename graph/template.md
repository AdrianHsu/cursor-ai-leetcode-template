# Graph Template

## Basic Structures

### 1. Adjacency List
```python
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
```

### 2. Edge List
```python
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
```

## Traversal Patterns

### 1. DFS (Depth-First Search)
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result
```

### 2. BFS (Breadth-First Search)
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

## Common Algorithms

### 1. Detect Cycle (Undirected)
```python
def has_cycle(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            # neighbor has been visited, and it is not parent.
            elif neighbor != parent:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False
```

### 2. Topological Sort
```python
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(graph) else []
```

### 3. Shortest Path (BFS)
```python
def shortest_path(graph, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        node, distance = queue.popleft()
        if node == end:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1
```

### 4. Has cycle directed version
```python
def has_cycle_directed(graph):
    visited = set()
    path = set()

    def dfs(node):
        if node in path:
            return True
        if node in visited:
            return False
        visited.add(node)
        path.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        
        path.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
```
TODO: Need an example question



## Key Techniques
- Use sets for visited tracking
- DFS for deep exploration
- BFS for shortest path (unweighted)
- Adjacency list for sparse graphs

