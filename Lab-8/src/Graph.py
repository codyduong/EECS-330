from collections import deque
from typing import List

class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices: int = vertices
        self.adjacency_list: List[List[int]] = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Add an edge between vertices u and v."""
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # For undirected graph

    def dfs(self, start_vertex: int) -> List[int]:
        """Depth-First Search traversal starting from the given vertex."""
        visited: List[bool] = [False] * self.vertices
        stack: List[int] = []
        result: List[int] = []

        stack.append(start_vertex)

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                result.append(vertex)
                visited[vertex] = True

            for neighbor in self.adjacency_list[vertex]:
                if not visited[neighbor]:
                    stack.append(neighbor)

        return result

    def bfs(self, start_vertex: int) -> List[int]:
        """Breadth-First Search traversal starting from the given vertex."""
        visited: List[bool] = [False] * self.vertices
        queue: deque[int] = deque()
        result: List[int] = []

        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            current_vertex: int = queue.popleft()
            result.append(current_vertex)

            for neighbor in self.adjacency_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result