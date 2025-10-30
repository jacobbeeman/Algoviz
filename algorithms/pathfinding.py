from collections import deque

class BFS:
    def __init__(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [], 'E': ['F'], 'F': []
        }
        self.start = 'A'

    def run(self):
        visited = set()
        queue = deque([self.start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                yield f"Visited: {node} | Queue: {list(queue)}"
                queue.extend(self.graph[node])
        yield f"Traversal complete: {visited}"


class DFS(BFS):
    def run(self):
        visited = set()
        stack = [self.start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                yield f"Visited: {node} | Stack: {stack}"
                stack.extend(reversed(self.graph[node]))
        yield f"Traversal complete: {visited}"