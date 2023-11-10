"""
Author: Cody Duong
KUID: 3050266
Date: 2023-11-09
Last modified: 2023-11-09
Purpose: Main file
"""
from src.Graph import Graph


if __name__ == "__main__":
    # Create a graph with 21 vertices.
    graph = Graph(21)

    # Add edges and their weights.
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 3, 3)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 5, 2)
    graph.add_edge(4, 6, 2)
    graph.add_edge(5, 7, 2)
    graph.add_edge(7, 8, 2)
    graph.add_edge(6, 8, 2)

    graph.add_edge(8, 9, 5)
    graph.add_edge(8, 10, 4)
    graph.add_edge(9, 11, 3)
    graph.add_edge(10, 11, 1)

    graph.add_edge(11, 12, 1)
    graph.add_edge(12, 13, 1)
    graph.add_edge(13, 14, 1)

    graph.add_edge(14, 15, 1)
    graph.add_edge(14, 16, 10)
    graph.add_edge(15, 17, 1)
    graph.add_edge(16, 20, 1)
    graph.add_edge(17, 18, 1)
    graph.add_edge(18, 19, 1)
    graph.add_edge(19, 20, 1)

    # Run Dijkstra's algorithm from source vertex 0.
    graph.dijkstra(0)

    # Find and print the Prim's Minimum Spanning Tree (MST).
    graph.prim()

    # Find and print the Kruskal's Minimum Spanning Tree (MST).
    graph.kruskal()
