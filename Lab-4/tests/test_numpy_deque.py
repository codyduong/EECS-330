"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-14
Lab: Lab4
Last modified: 2023-09-14
Purpose: Test ndarray deque functionality

Note that DequeNPNP is a subclass of DLList, and its generic is not type hinted correctly
for direct instantiation, and direct interactions with it require # type: ignore

C.1 Check whether the deque is empty
C.2 Check the size
C.3 Add element at front
C.4 Add element at the end
C.5 Remove element from the front
C.6 Remove element from the end
C.7 Access first element
C.8 Access last element
"""
from typing import Any, Callable, Type
import unittest
import numpy as np
from src.DLList import DLList


class Test_Numpy_Deque(unittest.TestCase):
    def __init__(self, *argv) -> None:
        super().__init__(*argv)
        self._empty_deque = DLList.DequeNP[str](capacity=10, dtype=np.dtype("U32"))

    def assertException(
        self, fn: Callable[..., Any], args: Any, error: Type[Exception]
    ) -> None:
        try:
            fn(*args)
        except Exception as e:
            # print(e)
            self.assertIsInstance(e, error)

    def test_empty(self) -> None:
        """C.1"""
        deque: "DLList.DequeNP[str]" = self._empty_deque
        self.assertEqual(len(deque), 0)
        self.assertEqual(deque.empty(), True)

    def test_suite1(self) -> None:
        """C.2, C.3, C.4, C.7, C.8"""
        deque: "DLList.DequeNP[str]" = self._empty_deque
        self.assertEqual(deque.get_size(), 0)
        deque.push_front("foo")  # type: ignore
        self.assertEqual(deque.front(), "foo")
        self.assertEqual(deque.get_size(), 1)
        deque.push_front("bar")  # type: ignore
        self.assertEqual(deque.back(), "foo")
        self.assertEqual(deque.front(), "bar")
        self.assertEqual(deque.get_size(), 2)
        deque.push("baz")  # type: ignore
        self.assertEqual(deque.back(), "baz")
        self.assertEqual(deque[2], "baz")
        self.assertEqual(deque[1], "foo")
        self.assertEqual(deque[0], "bar")
        self.assertEqual(deque.front(), "bar")
        self.assertEqual(deque.get_size(), 3)

    def test_b3(self) -> None:
        """C.3"""
        deque: "DLList.DequeNP[str]" = self._empty_deque
        self.assertEqual(deque.get_size(), 0)
        deque.push_front("foo")  # type: ignore
        self.assertEqual(deque.front(), "foo")
        self.assertEqual(deque.back(), "foo")
        deque.push_front("bar")  # type: ignore
        self.assertEqual(deque.front(), "bar")
        self.assertEqual(deque.back(), "foo")
        deque.push_front("baz")  # type: ignore
        self.assertEqual(deque.front(), "baz")
        self.assertEqual(deque.back(), "foo")

    def test_b4(self) -> None:
        """C.4"""
        deque: "DLList.DequeNP[str]" = self._empty_deque
        self.assertEqual(deque.get_size(), 0)
        deque.push("foo")  # type: ignore
        self.assertEqual(deque.back(), "foo")
        self.assertEqual(deque.front(), "foo")
        deque.push("bar")  # type: ignore
        self.assertEqual(deque.back(), "bar")
        self.assertEqual(deque.front(), "foo")
        deque.push("baz")  # type: ignore
        self.assertEqual(deque.back(), "baz")
        self.assertEqual(deque.front(), "foo")

    def test_b5(self) -> None:
        """C.5"""
        deque: "DLList.DequeNP[str]" = DLList.DequeNP(10, np.dtype("U32"), "foo", "bar", "baz")  # type: ignore
        self.assertEqual(deque, ["foo", "bar", "baz"])
        deque.pop_front()
        self.assertEqual(deque, ["bar", "baz"])
        deque.pop_front()
        self.assertEqual(deque, ["baz"])
        deque.pop_front()
        self.assertEqual(deque, [])
        # expect an error when attempting to remove items when there are none left
        self.assertException(deque.pop_front, [], IndexError)

    def test_b6(self) -> None:
        """C.6"""
        deque: "DLList.DequeNP[str]" = DLList.DequeNP(10, np.dtype("U32"), "foo", "bar", "baz")  # type: ignore
        self.assertEqual(deque, ["foo", "bar", "baz"])
        deque.pop()
        self.assertEqual(deque, ["foo", "bar"])
        deque.pop()
        self.assertEqual(deque, ["foo"])
        deque.pop()
        self.assertEqual(deque, [])
        # expect an error when attempting to remove items when there are none left
        self.assertException(deque.pop, [], IndexError)

    def test_suite2(self) -> None:
        """C.7, C.8"""
        deque: "DLList.DequeNP[str]" = DLList.DequeNP(10, np.dtype("U32"), "foo", "bar", "baz")  # type: ignore
        self.assertEqual(deque, ["foo", "bar", "baz"])
        self.assertEqual(deque.front(), "foo")
        self.assertEqual(deque.back(), "baz")
        deque.pop()
        self.assertEqual(deque.front(), "foo")
        self.assertEqual(deque.back(), "bar")
        deque.pop_front()
        self.assertEqual(deque.front(), "bar")
        self.assertEqual(deque.back(), "bar")
        deque.remove()
        self.assertEqual(deque.front(), None)
        self.assertEqual(deque.back(), None)

    def test_bounds(self) -> None:
        """Test if over capacity"""
        deque: "DLList.DequeNP[str]" = DLList.DequeNP(3, np.dtype("U32"), "foo", "bar", "baz")  # type: ignore
        self.assertException(deque.push, ["bang"], RuntimeError)
        self.assertException(deque.push_front, ["bang"], RuntimeError)
