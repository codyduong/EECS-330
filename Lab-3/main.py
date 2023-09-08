"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-07
Last modified: 2022-09-08
Purpose: Test cases for SLList.py

Notes:
* Uses built-in unittest framework for ease of testing
"""

import unittest

from typing import Any
from SLList import SLList


class TestSLList(unittest.TestCase):
    maxDiff: None = None

    def __init__(self, *argv: Any) -> None:
        super().__init__(*argv)

    def test_reverse(self) -> None:
        # 1.2 test addFirst and reverse

        L = SLList[int]()
        L.addFirst(15)
        L.addFirst(10)
        L.addFirst(5)
        L.reverse()

        L_expect = SLList[int]()
        L_expect.addFirst(5)
        L_expect.addFirst(10)
        L_expect.addFirst(15)

        self.assertEqual(L, L_expect)

    def test_reverse_recursive(self) -> None:
        # 1.4 test reverse with recursive

        L = SLList[int]()
        L.addFirst(15)
        L.addFirst(10)
        L.addFirst(5)
        L.reverse("recursive")

        L_expect = SLList[int]()
        L_expect.addFirst(5)
        L_expect.addFirst(10)
        L_expect.addFirst(15)

        self.assertEqual(L, L_expect)

    def test_insert(self) -> None:
        # 1.1 test insert

        L = SLList[int]()
        L.insert(1)
        L.insert(3)
        L.insert(2, 1)
        L.insert(4)

        L_expect = SLList[int]()
        L_expect.addFirst(4)
        L_expect.addFirst(3)
        L_expect.addFirst(2)
        L_expect.addFirst(1)

        self.assertEqual(L, L_expect)

    def test_replicate(self) -> None:
        # 1.3 test replicate

        L = SLList[int]()
        L.insert(3)
        L.insert(2)
        L.insert(1)
        L_expect = SLList[int]()
        L_expect.addFirst(1)
        L_expect.addFirst(2)
        L_expect.addFirst(3)

        self.assertEqual(L, L_expect)

        L2: SLList[int] = L.replicate()
        L2_expect = SLList[int]()
        L2_expect.addFirst(1)
        L2_expect.addFirst(2)
        L2_expect.addFirst(2)
        L2_expect.addFirst(3)
        L2_expect.addFirst(3)
        L2_expect.addFirst(3)

        self.assertEqual(L2, L2_expect)

    def test_replicate_error(self) -> None:
        # test mixed SLList type

        L = SLList[int]()
        L.insert("3")  # type: ignore
        L.insert(2)
        L.insert(1)
        L_not_expect = SLList[int]()
        L_not_expect.addFirst(1)
        L_not_expect.addFirst(2)
        L_not_expect.addFirst(3)
        L_expect = SLList[int]()
        L_expect.addFirst(1)
        L_expect.addFirst(2)
        L_expect.addFirst("3")  # type: ignore

        self.assertNotEqual(L, L_not_expect)
        self.assertEqual(L, L_expect)

        with self.assertRaises(TypeError):
            L.replicate()

    def test_insert_error(self) -> None:
        # test insert error
        L = SLList[int]()

        with self.assertRaises(IndexError):
            L.insert(3, -1)

        with self.assertRaises(IndexError):
            L.insert(3, 100)

        with self.assertRaises(TypeError):
            L.insert(3, "foo")  # type: ignore


if __name__ == "__main__":
    # Tests are written using unittest rather than print statements

    # Use the -v (verbose) flag to see specific test case results
    # ie `python main.py -v`
    unittest.main()
