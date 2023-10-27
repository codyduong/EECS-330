"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-25
Lab: Lab5
Last modified: 2023-09-27
Purpose: Test DisjointSet
"""


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.vertex: list[int] = [i for i in range(size)]
        self.weight: list[int] = [1] * size
        self.rank: list[int] = [0] * size

    def isValid(self) -> bool:
        for i in range(len(self.vertex)):
            if self.vertex[i] < 0 or self.vertex[i] >= len(self.vertex):
                return False
        return True

    def size(self) -> int:
        return len(self)

    def __len__(self) -> int:
        return len(self.vertex)

    def parent(self, v: int) -> int:
        if self.vertex[v] == v:
            return v
        else:
            return self.parent(self.vertex[v])

    def isConnected(self, v1: int, v2: int) -> bool:
        return self.parent(v1) == self.parent(v2)

    def find(self, v: int) -> int:
        if self.vertex[v] == v:
            return v
        else:
            root: int = self.find(self.vertex[v])
            if self.weight[v] > self.weight[self.vertex[v]]:
                self.vertex[root] = v
                self.weight[v] += self.weight[root]
            else:
                self.vertex[v] = root
                self.weight[root] += self.weight[v]
            return root

    def unionByWeight(self, v1: int, v2: int) -> None:
        root1: int = self.find(v1)
        root2: int = self.find(v2)

        if root1 == root2:
            # if we are already the same root, then we are done
            return

        if self.weight[root1] > self.weight[root2]:
            self.vertex[root2] = root1
            self.weight[root1] += self.weight[root2]
            # adjust the rank of root1
            self.rank[root1] = max(self.rank[root1], self.rank[root2] + 1)
        else:
            self.vertex[root1] = root2
            self.weight[root2] += self.weight[root1]
            # adjust the rank of root2
            self.rank[root2] = max(self.rank[root2], self.rank[root1] + 1)

    def unionByRank(self, v1: int, v2: int) -> None:
        p1: int = self.parent(v1)
        p2: int = self.parent(v2)
        if self.rank[p1] > self.rank[p2]:
            self.vertex[p2] = p1
        else:
            self.vertex[p1] = p2
            if self.rank[p1] == self.rank[p2]:
                self.rank[p2] += 1
            # Adjust the weight of p2
            self.weight[p2] += self.weight[p1]

    def joinBlocks(self, Connected: list[list[int]]) -> None:
        for i in range(len(Connected)):
            for j in range(len(Connected[0])):
                if Connected[i][j] == 1:
                    self.unionByRank(i, j)

    def findBlockSets(self) -> int:
        parents = set[int]()
        for i in range(len(self.vertex)):
            parents.add(self.parent(i))
        return len(parents)

    def findBlockCount(self, blockid: int) -> int:
        if not self.isValid():
            return 1
        parent: int = self.parent(blockid)
        count = 0
        for i in range(len(self.vertex)):
            if self.parent(i) == parent:
                count += 1
        return count

    def toCollection(self) -> list[set[int]]:
        parents = set[int]()
        for i in range(len(self.vertex)):
            parents.add(self.parent(i))
        components: list[list[int]] = []
        for parent in parents:
            component: list[int] = []
            for i in range(len(self.vertex)):
                if self.parent(i) == parent:
                    component.append(i)
            components.append(component)
        return [set(component) for component in components]
