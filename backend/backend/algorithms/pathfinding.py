# algorithms/pathfinding.py
from collections import deque

class BFS:
    def __init__(self):
        self.name = "Breadth-First Search"

    def run(self, graph, start):
        visited = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                queue.extend([n for n in graph[node] if n not in visited])
        return visited


class DFS:
    def __init__(self):
        self.name = "Depth-First Search"

    def run(self, graph, start, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                self.run(graph, neighbor, visited)
        return visited