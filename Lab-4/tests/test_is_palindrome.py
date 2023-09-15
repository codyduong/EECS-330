"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-14
Lab: Lab4
Last modified: 2023-09-14
Purpose: Test isPalindrome functionality

D. Implementation of isPalindrome using previously implemented deque
"""
import unittest
from src.isPalindrome import isPalindrome as is_palindrome

# the requirements say it is to be isPalindrome, so, it is isPalindrome 🤮


class Test_is_palindrome(unittest.TestCase):
    def test_true_1(self) -> None:
        self.assertTrue(is_palindrome("racecar"))

    def test_case_sensitivity_1(self) -> None:
        self.assertFalse(is_palindrome("Racecar"))

    def test_case_sensitivity_2(self) -> None:
        self.assertTrue(is_palindrome("RacecaR"))

    def test_true_2(self) -> None:
        self.assertTrue(is_palindrome("abut tuba"))

    def test_false_1(self) -> None:
        self.assertFalse(is_palindrome("foobar"))

    def test_false_2(self) -> None:
        self.assertFalse(is_palindrome("hello"))
