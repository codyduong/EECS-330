"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-21
Lab: Lab4
Last modified: 2023-09-21
Purpose: Test offByOne and offByN
"""
import unittest
from src.offByN import *
from src.offByOne import *


class Test_Off_By(unittest.TestCase):
    def test_off_by_one_1(self) -> None:
        self.assertTrue(offByOne("a", "b"))

    def test_off_by_one_2(self) -> None:
        self.assertTrue(offByOne("g", "f"))

    def test_off_by_one_3(self) -> None:
        self.assertFalse(offByOne("a", "h"))

    def test_off_by_one_4(self) -> None:
        self.assertFalse(offByOne("z", "a"))

    def test_off_by_n_1(self) -> None:
        self.assertTrue(offByN("a", "d", 3))

    def test_off_by_n_2(self) -> None:
        self.assertTrue(offByN("h", "e", 3))

    def test_off_by_n_3(self) -> None:
        self.assertFalse(offByN("a", "a", 3))

    def test_off_by_n_4(self) -> None:
        self.assertFalse(offByN("y", "a", 3))

    def test_off_by_one_all(self) -> None:
        # test 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(LETTERS) - 1):
            self.assertTrue(offByOne(LETTERS[i], LETTERS[i + 1]))
