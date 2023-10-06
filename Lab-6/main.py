"""
Author: Cody Duong
KUID: 3050266
Date: 2023-10-05
Last modified: 2023-10-05
Purpose: Main file
"""

from src.BinarySearchTree import BinarySearchTree, TreeMap


if __name__ == "__main__":
    # Initialize BST.
    bst = BinarySearchTree[int]()

    # Test inserting nodes
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)

    # Test size method.
    assert bst.size() == 7
    assert bst.search(1) == None

    assert bst.level_order_traversal() == [5, 3, 8, 2, 4, 7, 9]

    # Test inserting additional nodes.
    bst.insert(1)
    bst.insert(6)

    assert bst.size() == 9
    # it is possible the search fails, but it shouldn't so ignore this...
    assert bst.search(1).key == 1 # type: ignore

    # Test level order traversal.
    assert bst.level_order_traversal() == [5, 3, 8, 2, 4, 7, 9, 1, 6]

    # Finally, also test by inserting duplicate values.

    # Test level order traversal with duplicates.
    bst = BinarySearchTree[int]()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)
    bst.insert(5)
    bst.insert(7)
    bst.insert(1)
    bst.insert(6)
    bst.insert(1)
    bst.insert(6)

    # Test level order traversal.
    # print(bst._root_node)
    # print(bst._root_node.value) # 5
    # print(bst._root_node.left.value) # 3
    # print(bst._root_node.right.value) # 8
    # print(bst.level_order_traversal())
    assert bst.level_order_traversal() == [5, 3, 8, 2, 4, 7, 9, 1, 5, 7, 1, 6, 6]

    # TreeMap.

    # # Create a TreeMap
    tree_map = TreeMap()

    # Test putting and getting key-value pairs.
    tree_map.put(3, "A")
    tree_map.put(1, "B")
    tree_map.put(2, "C")
    tree_map.put(4, "D")

    # print(tree_map._root_node)
    # print(tree_map.get(2))
    assert tree_map.get(2) == "C"
    assert tree_map.get(1) == "B"
    assert tree_map.get(4) == "D"
    # Non-existent key should return None.
    assert tree_map.get(5) is None
