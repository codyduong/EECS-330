"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-25
Lab: Lab5
Last modified: 2023-09-27
Purpose: Test DisjointSet
"""
import unittest

from src.DisjointSet import DisjointSet


class Test_Disjoint_Set(unittest.TestCase):
    def test_task_a(self) -> None:
        # Tasks A
        uf = DisjointSet(10)
        # 0 1-2-5-6-7 3-8-9 4
        uf.unionByRank(1, 2)
        uf.unionByRank(2, 5)
        uf.unionByRank(5, 6)
        uf.unionByWeight(6, 7)
        uf.unionByRank(3, 8)
        uf.unionByWeight(8, 9)
        self.assertTrue(uf.isConnected(1, 5))
        self.assertTrue(uf.isConnected(5, 7))
        self.assertFalse(uf.isConnected(4, 9))
        rep: list[set[int]] = uf.toCollection()
        self.assertTrue({0} in rep)
        self.assertTrue({1, 2, 5, 6, 7} in rep)
        self.assertTrue({3, 8, 9} in rep)
        self.assertTrue({4} in rep)
        uf.unionByWeight(9, 4)
        rep: list[set[int]] = uf.toCollection()
        self.assertTrue({0} in rep)
        self.assertTrue({1, 2, 5, 6, 7} in rep)
        self.assertTrue({3, 8, 9, 4} in rep)
        self.assertTrue(uf.isConnected(4, 9))

    def test_task_b(self) -> None:
        Connected: list[list[int]] = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
        uf = DisjointSet(4)
        uf.joinBlocks(Connected)
        self.assertEqual(uf.findBlockCount(1), 4)