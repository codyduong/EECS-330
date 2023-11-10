"""
Author: Cody Duong
KUID: 3050266
Date: 2023-11-09
Last modified: 2023-11-09
Purpose: Graph pathfinding algos with dijkstra, prim, or kruskal
"""
import sys


class Graph:
    def __init__(self, vertices: int) -> None:
        self.V: int = vertices
        self.graph: list[list[int]] = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, w: int) -> None:
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, src: int) -> list[int]:
        # Stores shortest distance.
        dist: list[int] = [sys.maxsize] * self.V
        # Shortest distance to the same node is 0.
        dist[src] = 0

        # Your code.
        visited: list[bool] = [False] * self.V

        for _ in range(self.V):
            # Find the vertex with the minimum distance value
            min_dist = sys.maxsize
            min_dist_index = -1
            for v in range(self.V):
                if dist[v] < min_dist and not visited[v]:
                    min_dist: int = dist[v]
                    min_dist_index: int = v

            # Mark the picked vertex as visited
            visited[min_dist_index] = True

            # Update the distance value of the neighboring vertices
            for v in range(self.V):
                if (
                    self.graph[min_dist_index][v] > 0
                    and not visited[v]
                    and dist[v] > dist[min_dist_index] + self.graph[min_dist_index][v]
                ):
                    dist[v] = dist[min_dist_index] + self.graph[min_dist_index][v]

        # You have to call print_solution by passing dist.
        # In this way everyone's output would be standardized.
        self.print_dijkstra(dist)
        return dist

    def print_dijkstra(self, dist: list[int]) -> None:
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t->\t {dist[node]}")

    def prim(self) -> list[int]:
        # Store the resulting graph.
        # where result[i] keeps the source vertex.
        # See the example output for expected result.
        result: list[int] = [0] * self.V  # type: ignore

        # Your code.
        key: list[int] = [sys.maxsize] * self.V
        key[0] = 0
        mst_set: list[bool] = [False] * self.V

        for _ in range(self.V):
            # Find the vertex with the minimum key value
            min_key: int = sys.maxsize
            min_key_index = -1
            for v in range(self.V):
                if key[v] < min_key and not mst_set[v]:
                    min_key = key[v]
                    min_key_index = v

            # Add the picked vertex to the MST
            mst_set[min_key_index] = True

            # Update the key value of the neighboring vertices
            for v in range(self.V):
                if (
                    self.graph[min_key_index][v] > 0
                    and not mst_set[v]
                    and key[v] > self.graph[min_key_index][v]
                ):
                    key[v] = self.graph[min_key_index][v]
                    result[v] = min_key_index

        # You have to call print_solution by passing the output graph.
        # In this way everyone's output would be standardized.
        self.print_prim(result)
        return result

    def print_prim(self, result: list[int]) -> None:
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(f"{result[i]} - {i} \t {self.graph[i][result[i]]}")

    def find(self, parent: list[int], i: int) -> int:
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent: list[int], rank: list[int], x: int, y: int) -> None:
        x_root: int = self.find(parent, x)
        y_root: int = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self) -> list[tuple[int, int, int]]:
        # Your code.
        result: list[tuple[int, int, int]] = []
        i = 0
        e = 0
        edges: list[tuple[int, int, int]] = []

        for u in range(self.V):
            for v in range(u + 1, self.V):
                if self.graph[u][v] != 0:
                    edges.append((u, v, self.graph[u][v]))

        edges = sorted(edges, key=lambda x: x[2])

        parent: list[int] = [i for i in range(self.V)]
        rank: list[int] = [0] * self.V

        while e < self.V - 1:
            u, v, w = edges[i]
            i += 1
            x: int = self.find(parent, u)
            y: int = self.find(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        # Similar to the previous e.g. print your
        # resulting graph.
        self.print_kruskal(result)
        return result

    def print_kruskal(self, result: list[tuple[int, int, int]]) -> None:
        print("Edge \t Weight")
        # Note that the below code is slightly different than the Prim's.
        # You can change this print code according to your choice, but
        # you have to display your graph in (vertex->vertex weight) format.
        for edge in result:
            print(f"{edge[0]} -> {edge[1]} \t {edge[2]}")
