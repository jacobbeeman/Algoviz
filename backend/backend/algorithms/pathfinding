from collections import deque

def BFS(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return visited


def DFS(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)
    return visited