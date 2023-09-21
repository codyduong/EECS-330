"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-21
Lab: Lab4
Last modified: 2023-09-21
Purpose: Test word to deque functionality

E. Implementation of Deque Reversal
"""
import unittest
from src.DLList import DLList
from src.wordToDeque import wordToDeque as word_to_deque

def test_word_to_deque(
    test_string: str, test_deque: DLList.Deque[str]
) -> bool:
    for i in range(len(test_string)):
        try:
            if test_deque[i] != test_string[i]:
                return False
        except IndexError:
            return False

    return True

class Test_Word_To_Deque(unittest.TestCase):

    def assertWordToDeque(
        self, test_string: str, test_deque: DLList.Deque[str]
    ) -> None:
        self.assertTrue(test_word_to_deque(test_string, test_deque))

    def test_reverse_1(self) -> None:
        deque: DLList.Deque[str] = word_to_deque("abc")
        self.assertWordToDeque("abc", deque)
        self.assertEqual(deque, ["a", "b", "c"])

    def test_reverse_2(self) -> None:
        deque: DLList.Deque[str] = word_to_deque("0123456789")
        self.assertWordToDeque("0123456789", deque)
        self.assertEqual(deque, ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
