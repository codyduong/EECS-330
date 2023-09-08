"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-07
Last modified: 2022-09-08
Purpose: Single Linked List

Notes:
* Borrows code from my EECS-268 lab on LinkedList
* Heavy use of type-hinting
"""
from __future__ import annotations
from typing import Any, Generic, Literal, TypeVar, cast

T = TypeVar("T")


class SLList(Generic[T]):
    class Node(Generic[T]):  # type: ignore
        def __init__(self, item: T, next_node: "SLList.Node[T]" | None = None) -> None:
            self.item: T = item  # int
            self.next: SLList.Node[T] | None = next_node  # Node

        def __str__(self) -> str:
            return str(self.item)

    def __init__(self) -> None:
        self.first: "SLList.Node[T]" | None = None  # initialize an empty list
        self._len: int = 0

    def addFirst(self, item: T) -> None:
        self._len += 1
        self.first = self.Node(item, self.first)

    def insert(
        self,
        item: T,
        position: int | None = None,
    ) -> None:
        # if we don't specify a position, assume at the end
        if position == None:
            # if no items, just use addFirst
            if self.first == None:
                self.addFirst(item)
                return

            current_node: "SLList.Node[T]" = self.first  # type: ignore

            while current_node.next != None:
                current_node = current_node.next
            self._len += 1
            current_node.next = self.Node(item)

            return

        if position < 0 or position > len(self):
            raise IndexError

        if not isinstance(position, int):
            raise TypeError

        current_node: "SLList.Node[T]" | None = self.first
        # subtract 1 since range will add 1
        position = position - 1
        for _ in range(position):
            if current_node == None or current_node.next == None:
                raise IndexError
            current_node = current_node.next
        if current_node == None:
            raise IndexError
        old_next: "SLList.Node[T]" | None = current_node.next
        self._len += 1
        current_node.next = self.Node(item)
        if old_next:
            current_node.next.next = old_next

    def __reverse(
        self, node: "SLList.Node[T]", next: "SLList.Node[T]" | None = None
    ) -> "SLList.Node[T]":
        """
        Internal recursive reverse functionality
        """
        if node.next == None:
            node.next = next
            return node

        to_return: "SLList.Node[T]" = self.__reverse(node.next, node)
        node.next = next
        return to_return

    def reverse(
        self, method: Literal["iterative"] | Literal["recursive"] = "iterative"
    ) -> None:
        # reverse by going over and swapping around next
        current_node: "SLList.Node[T]" | None = self.first
        new_next: "SLList.Node[T]" | None = None

        if current_node == None:
            return

        if method != "recursive":
            # pylance conditional type checking gets confused due to type obsufucation from scoping issues,
            # so go ahead and redeclare this...
            current_node: "SLList.Node[T]" | None = self.first
            while current_node != None:
                temp: "SLList.Node[T]" = current_node
                if current_node.next == None:
                    current_node.next = new_next
                    self.first = current_node
                    break
                current_node = current_node.next
                temp.next = new_next
                new_next = temp
        else:
            self.first = self.__reverse(current_node)

    def replicate(self) -> "SLList[T]":
        replicated_list = SLList[T]()
        for item in self:
            if isinstance(item, int):
                for _ in range(item):
                    replicated_list.insert(item)
            else:
                raise TypeError("Expected node item type to be of int type")
        return replicated_list

    def __getitem__(self, index: int) -> T:
        if self.first == None:
            raise IndexError

        if index < 0 or index >= len(self):
            raise IndexError

        curr_node: "SLList.Node[T]" = self.first
        for _ in range(index):
            if curr_node and curr_node.next:
                curr_node = curr_node.next
        return curr_node.item

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> "SLList[T]":
        self.current_node: "SLList.Node[T]" | None = self.first
        return self

    def __next__(self) -> T:
        if self.current_node is not None:
            item: T = self.current_node.item
            self.current_node = self.current_node.next
            return item
        else:
            raise StopIteration

    def __str__(self) -> str:
        return f"[{', '.join(map(str, self))}]"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SLList):
            cast_other: "SLList[Any]" = cast(SLList[Any], other)
            if hasattr(cast_other, "__len__") and len(self) == len(cast_other):
                try:
                    for i in range(len(self)):
                        if self[i] != cast_other[i]:
                            return False
                except IndexError:
                    return False
                return True

        return False
