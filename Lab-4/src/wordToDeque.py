"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-21
Lab: Lab4
Last modified: 2023-09-21
Purpose: word to deque
"""

from .DLList import DLList


def wordToDeque(input: str) -> DLList.Deque[str]:
    # this works because Deque supports a iterable parameter in the constructor
    return DLList.Deque(*input)
