import unittest
from src.Graph import Graph


class TestGraph(unittest.TestCase):
    def test_dijkstra(self) -> None:
        g = Graph(5)
        g.add_edge(0, 1, 2)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 3, 7)
        g.add_edge(2, 4, 3)
        g.add_edge(3, 4, 1)

        dist: list[int] = g.dijkstra(0)

        # Expected output for Dijkstra's algorithm from source 0:
        # Vertex   Distance from Source
        # 0       ->       0
        # 1       ->       2
        # 2       ->       3
        # 3       ->       7
        # 4       ->       6
        expected_output: list[int] = [0, 2, 3, 7, 6]
        self.assertEqual(dist, expected_output)

    def test_prim(self) -> None:
        g = Graph(5)
        g.add_edge(0, 1, 2)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 3, 7)
        g.add_edge(2, 4, 3)
        g.add_edge(3, 4, 1)

        prim: list[int] = g.prim()

        # Expected output for Prim's algorithm:
        # Edge    Weight
        # 0 - 1   2
        # 1 - 2   1
        # 4 - 3   1
        # 2 - 4   3
        expected_output: list[int] = [0, 0, 1, 4, 2]
        self.assertEqual(prim, expected_output)

    def test_kruskal(self) -> None:
        g = Graph(5)
        g.add_edge(0, 1, 2)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 3, 7)
        g.add_edge(2, 4, 3)
        g.add_edge(3, 4, 1)

        kruskal: list[tuple[int, int, int]] = g.kruskal()

        # Expected output for Kruskal's algorithm:
        # Edge    Weight
        # 1 -> 2   1
        # 3 -> 4   1
        # 0 -> 1   2
        # 2 -> 4   3
        expected_output: list[tuple[int, int, int]] = [(1, 2, 1), (3, 4, 1), (0, 1, 2), (2, 4, 3)]
        self.assertEqual(kruskal, expected_output)


if __name__ == "__main__":
    unittest.main()
