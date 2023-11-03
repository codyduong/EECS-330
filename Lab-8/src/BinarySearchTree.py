"""
Author: Cody Duong
KUID: 3050266
Date: 2023-10-30
Last modified: 2023-11-02
Purpose: Binary Search Tree Node
Note: This code is directly taken from my 268 lab on BST's, modified to support required functionality
- Allow duplicate values (use right subtree)
"""


from typing import Any, Generic, List, Literal, TypeVar, Union

from src.TreeNode import TreeNode

BinarySearchTreeValue = TypeVar("BinarySearchTreeValue", bound="Any")


class BinarySearchTree(Generic[BinarySearchTreeValue]):
    def __init__(self) -> None:
        self._root_node: Union[
            TreeNode[BinarySearchTreeValue],
            None,
        ] = None
        # self._current_node: Union[
        #     BinarySearchTreeNode[BinarySearchTreeValue],
        #     None,
        # ] = None

    # add a simple getter/setter to follow the rules of the lab setup
    @property
    def root(
        self,
    ) -> Union[TreeNode[BinarySearchTreeValue], None,]:
        return self._root_node

    @root.setter
    def root(
        self,
        v: Union[
            TreeNode[BinarySearchTreeValue],
            None,
        ],
    ) -> None:
        self._root_node = v

    def _recursive_add(
        self,
        current_node: TreeNode[Any],
        new_node: TreeNode[Any],
    ) -> None:
        if current_node.value is None:
            current_node = new_node
        elif new_node < current_node:
            if current_node.left:
                self._recursive_add(current_node.left, new_node)
            else:
                current_node.left = new_node  # type: ignore
        elif new_node > current_node:
            if current_node.right:
                self._recursive_add(current_node.right, new_node)
            else:
                current_node.right = new_node  # type: ignore
        elif new_node == current_node:
            # raise ValueError(
            #     f"Duplicate value of: {new_node.value} was attempted to add to the BST, duplicate values are not allowed!"
            # )
            if current_node.right:
                self._recursive_add(current_node.right, new_node)
            else:
                current_node.right = new_node  # type: ignore
        else:
            raise RuntimeError(
                "An unknown exception occured while attempting to recursively add a node to the BST"
            )

    def add(self, value: BinarySearchTreeValue, key: int | None = None) -> None:
        root_node: TreeNode[BinarySearchTreeValue] | None = self._root_node
        new_node = TreeNode(
            key or value, value
        )  # this is stupid, but just use value as key, unless specified.
        if root_node is None:
            self._root_node = new_node
        else:
            return self._recursive_add(root_node, new_node)

    # functionality duplication for 330 lab
    def insert(self, value: BinarySearchTreeValue) -> None:
        return self.add(value)

    def level_order_traversal(self) -> list[BinarySearchTreeValue]:
        queue: list[TreeNode[BinarySearchTreeValue]] = []
        values: list[BinarySearchTreeValue] = []
        node: TreeNode[BinarySearchTreeValue] | None = self._root_node
        if node is not None:
            queue.append(node)

        while queue:
            node = queue.pop(0)
            values.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return values

    def _size_recursive(self, node: TreeNode[BinarySearchTreeValue] | None) -> int:
        if node is None:
            return 0

        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    # naive recursive implementation, maybe easier to keep track when adding and removing nodes... w/e
    def size(self) -> int:
        return self._size_recursive(self._root_node)

    def preorder(
        self,
        node: Union[
            None,
            TreeNode[Any],
        ] = None,
        order: List[BinarySearchTreeValue] | None = None,
    ) -> List[BinarySearchTreeValue]:
        """
        Return the preorder of the BST
        """
        order = [] if order is None else order
        root_node: TreeNode[BinarySearchTreeValue] | None = node or self._root_node
        if root_node:
            order.append(root_node.value)  # type: ignore

            if root_node.left:
                self.preorder(root_node.left, order)

            if root_node.right:
                self.preorder(root_node.right, order)

        return order

    # convenience wrapper omitting other args
    def preorder_traversal(self) -> List[BinarySearchTreeValue]:
        return self.preorder()

    def inorder(
        self,
        node: Union[
            None,
            TreeNode[Any],
        ] = None,
        order: List[BinarySearchTreeValue] | None = None,
    ) -> List[BinarySearchTreeValue]:
        """
        Return the inorder of the BST
        """
        order = [] if order is None else order
        root_node: TreeNode[BinarySearchTreeValue] | None = node or self._root_node
        if root_node:
            if root_node.left:
                self.inorder(root_node.left, order)

            order.append(root_node.value)  # type: ignore

            if root_node.right:
                self.inorder(root_node.right, order)

        return order

    # convenience wrapper omitting other args
    def inorder_traversal(self) -> List[BinarySearchTreeValue]:
        return self.inorder()

    def postorder(
        self,
        node: Union[
            None,
            TreeNode[Any],
        ] = None,
        order: List[BinarySearchTreeValue] | None = None,
    ) -> List[BinarySearchTreeValue]:
        """
        Return the postorder of the BST
        """
        order = [] if order is None else order
        root_node: TreeNode[BinarySearchTreeValue] | None = node or self._root_node
        if root_node:
            if root_node.left:
                self.postorder(root_node.left, order)

            if root_node.right:
                self.postorder(root_node.right, order)

            order.append(root_node.value)  # type: ignore

        return order

    # convenience wrapper omitting other args
    def postorder_traversal(self) -> List[BinarySearchTreeValue]:
        return self.postorder()

    def search(
        self,
        value: Any,  # indexed access types where?
        *keys: str,
        current_node: Union[TreeNode[Any], None, Literal[False]] = None,
    ) -> Union[TreeNode[BinarySearchTreeValue], None]:
        """
        This search function will return a whole node based on a subkey path.

        @deprecated, i forget the pydoc semantics w/e, ignore description

        :value: any value to search for
        :key: property to access on node
        :example:
            pokedex.search(132, "id") # -> ditto

        """
        current_node = self._root_node if current_node is None else current_node

        if not current_node:
            return None

        current_value: TreeNode[BinarySearchTreeValue] = current_node
        # if current_value is None:
        #     return None

        # set keys by default to access value
        keys = ("value",) if len(keys) == 0 else keys

        for k in keys:
            # Of course this is unsafe
            current_value = getattr(current_value, k)  # type: ignore

        if value == current_value:
            return current_node
        elif value < current_value:
            return self.search(
                value,
                *keys,
                current_node=current_node.left if current_node.left else False,
            )
        elif value > current_value:
            return self.search(
                value,
                *keys,
                current_node=current_node.right if current_node.right else False,
            )

    def _copy(
        self,
        current_node: Union[TreeNode[Any], None] = None,
    ) -> TreeNode[Any]:
        raise NotImplementedError
        # deprecated from 268 lab

        """Copy the binary search tree, must reimplement for superclasses"""
        current_node = current_node or self._root_node

        root_copy: TreeNode[Any] = TreeNode(None)
        if current_node:
            root_copy = TreeNode(current_node.value)
            if current_node.left:
                root_copy.left = self._copy(current_node.left)  # type: ignore
            if current_node.right:
                root_copy.right = self._copy(current_node.right)  # type: ignore

        return root_copy

    def copy(self) -> Any:
        copied_tree: BinarySearchTree[Any] = BinarySearchTree()
        copied_tree._root_node = self._copy(self._root_node)
        return copied_tree

    def _min_value_node(self, node: TreeNode[Any]) -> TreeNode[Any]:
        current: TreeNode[Any] = node
        while current.left is not None:
            current = current.left

        return current

    def remove(
        self,
        value: Any,
        *keys: str,
        current_node: Union[TreeNode[Any], None, Literal[False]] = None,
    ) -> Union[TreeNode[Any], None]:
        raise NotImplementedError
        # deprecated from 268 lab

        """
        Remove a node

        Returns a the new node after removal

        :value: any value to search for
        :key: property to access on node
        :example:
            pokedex.remove(12) # -> "Butterfree"
        """
        current_node = self._root_node if current_node is None else current_node

        if not current_node:
            return None

        current_value: TreeNode[BinarySearchTreeValue] = current_node.value
        if current_value is None:
            return None

        for k in keys:
            # Of course this is unsafe
            current_value = getattr(current_value, k)  # type: ignore

        # print(value, current_value)

        if value < current_value:
            current_node.left = self.remove(value, *keys, current_node=current_node.left if current_node.left else False)  # type: ignore
        elif value > current_value:
            current_node.right = self.remove(value, *keys, current_node=current_node.right if current_node.right else False)  # type: ignore
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp

            temp = self._min_value_node(current_node.right)

            current_node.value = temp.value
            temp_value_compare = temp.value
            for k in keys:
                temp_value_compare = getattr(temp_value_compare, k)

            current_node.right = self.remove(temp_value_compare, *keys, current_node=current_node.right if current_node.right else False)  # type: ignore

        return current_node
