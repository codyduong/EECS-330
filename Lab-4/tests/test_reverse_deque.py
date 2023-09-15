"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-14
Lab: Lab4
Last modified: 2023-09-14
Purpose: Test ndarray deque functionality

E. Implementation of Deque Reversal
"""
import unittest
from src.DLList import DLList
from src.reverse_deque import reverse_deque


class Test_Reverse_Deque(unittest.TestCase):
    def test_reverse_1(self) -> None:
        deque: "DLList.Deque[str]" = DLList.Deque("foo", "bar", "baz")  # type: ignore
        self.assertEqual(reverse_deque(deque), ["baz", "bar", "foo"])

    def test_reverse_2(self) -> None:
        deque: "DLList.Deque[str]" = DLList.Deque(*range(100))  # type: ignore
        self.assertEqual(reverse_deque(deque), list(reversed(range(100))))
