"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-14
Last modified: 2023-09-14
Purpose: Double Linked List with Deque Implementations (etiher via Node with prev/next or via numpy ndarray)

Notes:
* Borrows code from my EECS-268 lab on LinkedList
* Heavy use of type-hinting
"""
from __future__ import annotations
from typing import (
    Any,
    Callable,
    Generic,
    Iterable,
    Literal,
    TypeGuard,
    TypeVar,
    Union,
    cast,
)

import numpy as np
from .assertx import assertx

T = TypeVar("T")


class DLList(Generic[T]):
    class Node(Generic[T]):  # type: ignore
        """
        This node implementation with the ability to link and unlink previous/next nodes
        """

        def __init__(
            self,
            value: T,
            prev: "DLList.Node[T]" | None = None,
            next: "DLList.Node[T]" | None = None,
        ) -> None:
            """
            :param value: The value of the node
            :param prev: Optional. Set the previous node
            :param next: Optional. Set the next node
            """
            self._value: T = value
            self._next: "DLList.Node[T]" | None
            self._prev: "DLList.Node[T]" | None
            self.link_prev(prev)
            self.link_next(next)

        @property
        def value(self) -> T:
            return self._value

        @property
        def prev(self) -> "DLList.Node[T]" | None:
            return self._prev

        @property
        def next(self) -> "DLList.Node[T]" | None:
            return self._next

        @value.setter
        def value(self, value: T) -> None:
            self._value = value

        def link_prev(self, prev_node: "DLList.Node[T]" | None) -> None:
            """
            Links the previous pointer towards another Node, and also sets that Node's forwards pointer to this Node

            :param prev_node: Node instance
            """
            self._prev: "DLList.Node[T]" | None = prev_node
            if prev_node and prev_node._next is None:
                prev_node.link_next(self)

        def link_next(self, next_node: "DLList.Node[T]" | None) -> None:
            """
            Links the forwards pointer towards another Node, and also sets that Node's previous pointer to this Node

            :param prev_node: Node instance
            """
            self._next: "DLList.Node[T]" | None = next_node
            if next_node and next_node._prev is None:
                next_node.link_prev(self)

        def unlink_prev(self) -> None:
            """
            Unlinks the forwards pointer towards another Node, and also sets that Node's previous pointer to this None

            :param prev_node: Node instance
            """
            if self._prev and self._prev._next:
                self._prev._next = None
            self._prev = None

        def unlink_next(self) -> None:
            """
            Unlinks the previous pointer towards another Node, and also sets that Node's forwards pointer to this None

            :param prev_node: Node instance
            """
            if self._next and self._next._prev:
                self._next._prev = None
            self._next = None

        def __str__(self) -> str:
            return str(self._value)

        @staticmethod
        def isinstance(arg: Any) -> "TypeGuard[DLList.Node[T]]":
            """Typeguards if it is an own instance, see PEP-0647"""
            return isinstance(arg, DLList.Node)

    class Deque(Generic[T]):  # type: ignore
        def __init__(self, *argv: Union[DLList[T], T, Iterable[T]]):
            self._front: "DLList.Node[T]" | None = None
            self._back: "DLList.Node[T]" | None = None
            self._size = 0

            if len(argv) > 0:
                for arg in argv:
                    if DLList.Node.isinstance(arg):
                        raise TypeError(
                            "Node instances are not supported, they are automatically instantiated by LinkedList"
                        )
                    else:
                        # does this cause errors? w/e TODO
                        self.append(arg)  # type: ignore

        def empty(self) -> bool:
            return self._size == 0

        def front(self) -> T | None:
            return self._front and self._front.value

        def back(self) -> T | None:
            return self._back and self._back.value

        def get_size(self) -> int:
            """
            A convenience method around __len__, recommended to use len(...) instead

            :returns: Integer of list length
            """
            return len(self)

        def __len__(self) -> int:
            return self._size

        def __set_head_tail(self) -> None:
            """
            Private helper method to set the TAIL to HEAD or HEAD to TAIL if length is only 1

            Also will set both TAIL and HEAD to None if size is 0
            """
            if len(self) == 1:
                # Probably a bit unidiomatic... w/e
                self._back = self._back or self._front
                self._front = self._front or self._back
            elif len(self) == 0:
                # also unidiomatic, ideally this shouldn't need to be done here but its easier here...
                self._back = None
                self._front = None

        def append(self, value: T) -> None:
            """
            Append an element to the TAIL of the LinkedList

            :param value: value to insert
            """
            new_tail = DLList.Node(value, self._back)
            if self._back:
                self._back.link_next(new_tail)
            self._back = new_tail
            self._size += 1
            self.__set_head_tail()

        def push(self, value: T) -> None:
            return self.append(value)

        def insert(self, value: T, index: int = 0) -> None:
            """
            Insert an element at an index, by default is at HEAD

            :param value: value to insert
            :param index: to insert element at, by default inserts at HEAD
            """
            assertx(isinstance(index, int), TypeError, "index is not of type int")

            if index > len(self):
                raise IndexError(
                    f"Index out of bounds, maximum index surpassed at: {len(self)}"
                )
            elif index < 0:
                raise IndexError()
            elif index == 0:
                new_head = DLList.Node(value, next=self._front)
                self._front = new_head
                self._size += 1
            elif index == len(self):
                self.append(value)
            else:
                curr_node = self._front
                for _ in range(index):
                    curr_node = curr_node._next  # type: ignore
                else:
                    curr_node.link_next(self.Node(value, next=curr_node._next))  # type: ignore
                    self._size += 1
            self.__set_head_tail()

        def push_front(self, value: T) -> None:
            """
            A convenience method around insert

            :return: None
            """
            return self.insert(value)

        def pop(self, index: int | None = None) -> None:
            """
            Remove an element at an index, by default is at TAIL

            :param index: index to insert element at, by default removes at TAIL
            :return: The value of the element that was popped
            """
            max_len = len(self) - 1
            if index is None:
                index = max_len

            assertx(isinstance(index, int), TypeError, f"index is not of type int")

            if index > max_len:
                raise IndexError(
                    f"Index out of bounds, maximum index surpassed at: {max_len}"
                )
            elif index < 0:
                raise IndexError("Index cannot be negative")
            elif index == 0:
                temp_next = self._front._next  # type: ignore
                self._front.unlink_next()  # type: ignore
                self._front = temp_next
            elif index == max_len:
                temp_prev = self._back._prev  # type: ignore
                self._back.unlink_prev()  # type: ignore
                self._back = temp_prev
            self._size -= 1
            self.__set_head_tail()

        def remove(self, index: int = 0) -> T:
            """
            Remove an element at an index, by default is at HEAD

            :param index: index to insert element at, by default removes at HEAD
            :return: The value of the element that was popped
            """
            return self.pop(index)  # type: ignore

        def pop_front(self) -> T:
            """
            A convenience method around remove

            :return: None
            """
            return self.remove()

        def __iterate_to(
            self,
            index: Union[int, slice],
            callback: Callable[[Union[DLList[T], DLList.Node[T], None]], None],
        ) -> Any:
            """
            Helper function for __getitem__ and __setitem__, uses a callback to do an action on any elem in list.
            """

            is_int: bool = isinstance(index, int)
            is_slice: bool = isinstance(index, slice)

            assertx(
                is_int or is_slice,
                TypeError,
                "index is not of type int or slice",
            )

            curr_node: DLList.Node[T] | None = self._front
            try:
                if is_int:
                    # if index is less than half start from the front
                    if index <= len(self) // 2:
                        for _ in range(index):
                            if curr_node and curr_node._next:
                                curr_node = curr_node._next
                    # if index is greater than half start from the back
                    else:
                        curr_node = self._back
                        for _ in range(len(self) - index - 1):
                            if curr_node and curr_node._prev:
                                curr_node = curr_node._prev
                    return callback(curr_node)

                elif is_slice:
                    # FROM EECS268 LAB, removed
                    raise NotImplementedError

                    # temp_list = DLList[T]()
                    # start = index.start or 0
                    # stop = index.stop or len(self)
                    # step = index.step or 1
                    # assertx(
                    #     start >= 0,
                    #     ValueError,
                    #     "Slicing with negative numbers is not supported",
                    # )
                    # assertx(
                    #     stop >= 0,
                    #     ValueError,
                    #     "Slicing with negative numbers is not supported",
                    # )
                    # assertx(
                    #     step >= 0,
                    #     ValueError,
                    #     "Slicing with negative numbers is not supported",
                    # )
                    # for i in range(stop):
                    #     if i >= start and (i + start) % step == 0:
                    #         temp_list.append(curr_node.value) # type: ignore
                    #     if curr_node and curr_node._next:
                    #         curr_node = curr_node._next

                    # return callback(temp_list)
            except AttributeError as e:
                """
                ...raises a RuntimeError otherwise. Ideally we'd cover this with the proper errors,
                typically an IndexError, but it's explicitly stated otherwise on the lab reqs. w/e
                """
                raise RuntimeError(e)

        def __getitem__(self, index: Union[int, slice]) -> T:
            """
            Only supports 0 to index length inclusive,
            Slicing is implemented but does not support negative ints
            """

            return self.__iterate_to(
                index,
                lambda node_or_list: node_or_list.value
                if isinstance(node_or_list, DLList.Node)
                else node_or_list,  # type: ignore
            )

        def __setitem__(self, index: int, value: T) -> None:
            """
            Only supports 0 to index length inclusive,
            Slicing is not implemented/supported
            """
            assertx(
                isinstance(index, int),
                TypeError,
                "index is not of type int",
            )

            def set_item_callback(node: DLList.Node[T]) -> None:
                node.value = value

            return self.__iterate_to(index, set_item_callback)  # type: ignore

        def __iter__(self) -> "DLList.Deque[T]":
            self.current_node: "DLList.Node[T]" | None = self._front
            return self

        def __next__(self) -> T:
            if self.current_node is not None:
                item: T = self.current_node.value
                self.current_node = self.current_node._next
                return item
            else:
                raise StopIteration

        def __add__(self, other: "DLList.Deque[T]" | T) -> "DLList.Deque[T]":
            temp_deque = self
            if isinstance(other, DLList.Deque):
                for elem in other:
                    temp_deque.append(elem)
            else:
                temp_deque.append(other)
            return temp_deque

        def __str__(self) -> str:
            output_str = "["
            for elem in self:
                output_str += f"{elem}, "
            output_str: str = output_str[:-2]
            output_str += "]"
            return output_str

        def __eq__(self, other: object) -> bool:
            if isinstance(other, DLList.DequeNP) or isinstance(other, Iterable):
                cast_other: "DLList.DequeNP[Any]" = cast(DLList.DequeNP[Any], other)
                if hasattr(cast_other, "__len__") and len(self) == len(cast_other):
                    try:
                        for i in range(len(self)):
                            # print(i, self[i], cast_other[i])
                            if self[i] != cast_other[i]:
                                return False
                    except IndexError:
                        return False
                    return True

            return False

        def resize(self) -> None:
            raise NotImplementedError

    class DequeNP(Generic[T]):  # type: ignore
        def __init__(
            self, capacity: int, dtype: Any, *argv: Union[DLList[T], T, Iterable[T]]
        ) -> None:
            self._front: int = -1
            self._back: int = -1
            self._size: int = 0
            self._capacity: int = capacity
            self._array = np.zeros(capacity, dtype=np.dtype("U32"))

            if len(argv) > 0:
                for arg in argv:
                    if DLList.Node.isinstance(arg):
                        raise TypeError(
                            "Node instances are not supported, they are automatically instantiated by LinkedList"
                        )
                    else:
                        # does this cause errors? w/e TODO
                        self.append(arg)  # type: ignore

        def empty(self) -> bool:
            return self._size == 0

        def front(self) -> T | None:
            return None if self._front == -1 else self._array[self._front]

        def back(self) -> T | None:
            return None if self._back == -1 else self._array[self._back]

        def get_size(self) -> int:
            """
            A convenience method around __len__, recommended to use len(...) instead

            :returns: Integer of list length
            """
            return len(self)

        def __len__(self) -> int:
            return self._size

        def __handle_size(self) -> None:
            """Handle setting front/back on size changes"""
            if self._size < 1:
                self._front = -1
                self._back = -1
            elif self._size == 1:
                self._front = 0
                self._back = 0
            else:
                self._front = 0
                self._back = self._size - 1

        def append(self, value: T) -> None:
            """
            Append an element to the TAIL of the LinkedList

            :param value: value to insert
            """
            new_size: int = self._size + 1
            if new_size > self._capacity:
                raise RuntimeError("Capacity reached, cannot push item to back")
            self._array[new_size - 1] = value
            self._size += 1
            self.__handle_size()

        def push(self, value: T) -> None:
            return self.append(value)

        def insert(self, value: T, index: int = 0) -> None:
            """
            Not required for implementation in this EECS 330 Lab
            """
            raise NotImplementedError

        def push_front(self, value: T) -> None:
            """
            Push to front

            :return: None
            """
            if self._size == self._capacity:
                raise RuntimeError("Capacity reached, cannot push item to front")

            # shift rightwards
            self._array[1:] = self._array[:-1]
            self._array[0] = value
            self._size += 1
            self.__handle_size()

        def pop(self, index: int | None = None) -> None:
            """
            Remove an element at an index, by default is at TAIL

            :param index: index to insert element at, by default removes at TAIL
            :return: The value of the element that was popped
            """
            max_len = len(self) - 1
            if index is None:
                index = max_len

            assertx(isinstance(index, int), TypeError, f"index is not of type int")

            if index > max_len:
                raise IndexError(
                    f"Index out of bounds, maximum index surpassed at: {max_len}"
                )
            elif index < 0:
                raise IndexError("Index cannot be negative")
            old_array = self._array
            # remove the index
            self._array[:index] = old_array[:index]
            # fill from right, making sure the rightmost item spot is still filled with empty data
            self._array[index:] = np.append(
                old_array[index + 1 :], np.zeros(1, dtype=self._array.dtype)
            )
            self._size -= 1
            self.__handle_size()

        def remove(self, index: int = 0) -> T:
            """
            Remove an element at an index, by default is at HEAD

            :param index: index to insert element at, by default removes at HEAD
            :return: The value of the element that was popped
            """
            return self.pop(index)  # type: ignore

        def pop_front(self) -> T:
            """
            A convenience method around remove

            :return: None
            """
            return self.remove()

        def __getitem__(self, index: int) -> T:
            return self._array[index]

        def __setitem__(self, index: int, value: T) -> None:
            self._array[index] = value

        def __iter__(self) -> "DLList.DequeNP[T]":
            self.step: int = self._front
            return self

        def __next__(self) -> T:
            # this is stupid and dumb and noone should write code like this
            if self.step == -1 or (self.step >= self._size):
                raise StopIteration
            try:
                item = self[self.step]
            except IndexError:
                raise StopIteration
            self.step += 1
            if item is None:
                raise StopIteration
            return item

        def __str__(self) -> str:
            output_str = "["
            for elem in self:
                output_str += f"{elem}, "
            output_str: str = output_str[:-2]
            output_str += "]"
            return output_str

        def __eq__(self, other: object) -> bool:
            if isinstance(other, DLList.Deque) or isinstance(other, Iterable):
                cast_other: "DLList.Deque[Any]" | "DLList.DequeNP[Any]" = cast(
                    DLList.Deque[Any], other
                )
                if hasattr(cast_other, "__len__") and len(self) == len(cast_other):
                    try:
                        for i in range(len(self)):
                            # print(i, self[i], cast_other[i])
                            if self[i] != cast_other[i]:
                                return False
                    except IndexError:
                        return False
                    return True

            return False

        def resize(self) -> None:
            """Doubles capacity as specified by requirements"""
            self._capacity = self._capacity * 2

            old_array = self._array
            self._array = np.zeros(self._capacity, dtype=self._array.dtype)
            self._array[: self._size] = old_array

    def __init__(
        self,
        method: Literal["linkedlist"] | Literal["ndarray"] = "linkedlist",
        dtype: Any = None,
        capacity: Any = None,
        *argv: Union[DLList[T], T, Iterable[T]],
    ) -> None:
        """
        Initialize a linked list with elements (optional)

        :param method: Defaults to linkedlist
        :param capacity: Required if using method="ndarray", integer
        :param dtype: Required if using method="ndarray", see: https://numpy.org/doc/stable/reference/arrays.dtypes.html
        :param items: Optional. Accepts individual elements (not in a Node).
        """
        if method == "ndarray" and dtype == None:
            raise ValueError("If using ndtype, the dtype parameter must be specified")

        self._deque: "DLList.Deque[T] | DLList.DequeNP[T]" = (
            self.Deque(*argv)
            if method == "linkedlist"
            else self.DequeNP(capacity, dtype, *argv)  # type: ignore
        )

    def empty(self) -> bool:
        return self._deque.empty()

    def front(self) -> T | None:
        return self._deque.front()

    def back(self) -> T | None:
        return self._deque.back()

    def append(self, value: T) -> None:
        """
        Append an element to the TAIL of the LinkedList

        :param value: value to insert
        """
        self._deque.append(value)

    def push(self, value: T) -> None:
        return self.append(value)

    def insert(self, value: T, index: int = 0) -> None:
        """
        Insert an element at an index, by default is at HEAD

        :param value: value to insert
        :param index: to insert element at, by default inserts at HEAD
        """
        self._deque.insert(value, index)

    def push_front(self, value: T) -> None:
        """
        A convenience method around insert

        :return: None
        """
        return self.insert(value)

    def pop(self, index: int | None = None) -> None:
        """
        Remove an element at an index, by default is at TAIL

        :param index: index to insert element at, by default removes at TAIL
        :return: The value of the element that was popped
        """
        return self._deque.pop(index)

    def remove(self, index: int = 0) -> T:
        """
        Remove an element at an index, by default is at HEAD

        :param index: index to insert element at, by default removes at HEAD
        :return: The value of the element that was popped
        """
        return self.pop(index)  # type: ignore

    def pop_front(self) -> T:
        """
        A convenience method around remove

        :return: None
        """
        return self.remove()

    def __getitem__(self, index: Union[int, slice]) -> T:
        """
        Only supports 0 to index length inclusive
        """
        return self._deque.__getitem__(index)

    def __setitem__(self, index: int, value: T) -> None:
        """
        Only supports 0 to index length inclusive,
        Slicing is not implemented/supported
        """
        return self._deque.__setitem__(index, value)

    def __iter__(self) -> "DLList[T]":
        self.current_node: "DLList.Node[T]" | None | int = self._deque._front
        return self

    def __next__(self) -> T:
        if isinstance(self.current_node, int):
            if self.current_node == -1:
                raise StopIteration
            item = self._deque._array = self[self.current_node]
            self.current_node += 1
            if item is None:
                raise StopIteration
            return item
        elif self.current_node is not None:
            item: T = self.current_node.value
            self.current_node = self.current_node._next
            return item
        else:
            raise StopIteration

    def __add__(self, other: "DLList[T]" | T) -> "DLList[T]":
        temp_list = self
        if isinstance(other, DLList):
            for elem in other:
                temp_list.append(elem)
        else:
            temp_list.append(other)
        return temp_list

    def __str__(self) -> str:
        output_str = "["
        for elem in self:
            output_str += f"{elem}, "
        output_str: str = output_str[:-2]
        output_str += "]"
        return output_str

    def __eq__(self, other: object) -> bool:
        return self._deque.__eq__(other)

    @staticmethod
    def isinstance(arg: Any) -> "TypeGuard[DLList[T]]":
        """Typeguards if it is an own instance, see PEP-0647"""
        return isinstance(arg, DLList)
