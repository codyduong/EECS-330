from typing import Any
import unittest
from src.BinarySearchTree import BinarySearchTree
from src.TreeNode import TreeNode


class TestBinarySearchTree(unittest.TestCase):
    maxDiff = None

    def __init__(self, *argv: Any) -> None:
        super().__init__(*argv)

        test_bst1: BinarySearchTree[int] = BinarySearchTree()
        test_bst1.add(50)
        test_bst1.add(25)
        test_bst1.add(75)
        test_bst1.add(12)
        test_bst1.add(37)
        self.test_bst1: BinarySearchTree[int] = test_bst1

        test_bst2 = BinarySearchTree[int]()
        test_bst2.root = TreeNode(1)  # type: ignore
        test_bst2.root.left = TreeNode(2)  # type: ignore
        test_bst2.root.right = TreeNode(3)  # type: ignore
        test_bst2.root.left.left = TreeNode(4)  # type: ignore
        test_bst2.root.left.right = TreeNode(5)  # type: ignore
        test_bst2.root.right.left = TreeNode(6)  # type: ignore
        test_bst2.root.right.right = TreeNode(7)  # type: ignore
        test_bst2.root.left.left.left = TreeNode(8)  # type: ignore
        test_bst2.root.left.left.right = TreeNode(9)  # type: ignore
        test_bst2.root.right.right.right = TreeNode(10)  # type: ignore

        self.test_bst2: BinarySearchTree[int] = test_bst2

    def test_preorder(self) -> None:
        self.assertListEqual(self.test_bst1.preorder(), [50, 25, 12, 37, 75])

    def test_inorder(self) -> None:
        self.assertListEqual(self.test_bst1.inorder(), [12, 25, 37, 50, 75])

    def test_postorder(self) -> None:
        self.assertListEqual(self.test_bst1.postorder(), [12, 37, 25, 75, 50])

    def test_lab8(self) -> None:
        self.assertListEqual(
            self.test_bst2.preorder_traversal(), [1, 2, 4, 8, 9, 5, 3, 6, 7, 10]
        )
        self.assertListEqual(
            self.test_bst2.inorder_traversal(), [8, 4, 9, 2, 5, 1, 6, 3, 7, 10]
        )
        self.assertListEqual(
            self.test_bst2.postorder_traversal(), [8, 9, 4, 5, 2, 6, 10, 7, 3, 1]
        )


if __name__ == "__main__":
    unittest.main()
