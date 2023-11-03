"""
Author: Cody Duong
KUID: 3050266
Date: 2023-11-02
Last modified: 2023-11-02
Purpose: Main file
"""
from src.BinarySearchTree import BinarySearchTree
from src.TreeNode import TreeNode
from src.Graph import Graph


if __name__ == "__main__":
    # Create a binary tree
    bt = BinarySearchTree[int]()
    bt.root = TreeNode(1)  # type: ignore
    bt.root.left = TreeNode(2)  # type: ignore
    bt.root.right = TreeNode(3)  # type: ignore
    bt.root.left.left = TreeNode(4)  # type: ignore
    bt.root.left.right = TreeNode(5)  # type: ignore
    bt.root.right.left = TreeNode(6)  # type: ignore
    bt.root.right.right = TreeNode(7)  # type: ignore
    bt.root.left.left.left = TreeNode(8)  # type: ignore
    bt.root.left.left.right = TreeNode(9)  # type: ignore
    bt.root.right.right.right = TreeNode(10)  # type: ignore

    # Test the traversals
    print("Preorder Traversal:", bt.preorder_traversal())
    print("Inorder Traversal:", bt.inorder_traversal())
    print("Postorder Traversal:", bt.postorder_traversal())

    # Create a graph with 20 vertices
    graph = Graph(20)

    # Add edges (change as needed)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    graph.add_edge(3, 7)
    graph.add_edge(3, 8)
    graph.add_edge(4, 9)
    graph.add_edge(4, 10)
    graph.add_edge(5, 11)
    graph.add_edge(5, 12)
    graph.add_edge(6, 13)
    graph.add_edge(6, 14)
    graph.add_edge(7, 15)
    graph.add_edge(7, 16)
    graph.add_edge(8, 17)
    graph.add_edge(8, 18)
    graph.add_edge(9, 19)

    # Test DFS and BFS from a source vertex
    print("DFS from vertex 0:", graph.dfs(0))
    print("BFS from vertex 0:", graph.bfs(0))

    # Create a graph with 4 vertices
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    # Test DFS and BFS from a source vertex
    print("DFS from vertex 2:", graph.dfs(2))
    print("BFS from vertex 2:", graph.bfs(2))
