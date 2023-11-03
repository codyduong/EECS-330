from typing import Any, List
import unittest
from src.Graph import Graph


class TestGraphTraversal(unittest.TestCase):
    def __init__(self, *argv: Any) -> None:
        super().__init__(*argv)

        self.graph = Graph(7)
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(2, 5)
        self.graph.add_edge(2, 6)

    def test_dfs(self) -> None:
        dfs_result: List[int] = self.graph.dfs(0)
        self.assertEqual(dfs_result, [0, 2, 6, 5, 1, 4, 3])

    def test_bfs(self) -> None:
        bfs_result: List[int] = self.graph.bfs(0)
        self.assertEqual(bfs_result, [0, 1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
