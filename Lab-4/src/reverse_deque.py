"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-14
Lab: Lab4
Last modified: 2023-09-14
Purpose: Reverse Deque
"""

from typing import TypeVar
from .DLList import DLList

T = TypeVar("T")


def reverse_deque(deque: DLList.Deque[T]) -> DLList.Deque[T]:
    # Initialize an object for your new deque.
    reversed_deque = DLList.Deque[T]()

    for i in range(len(deque)):
        # this works since we specify a __getitem__ on Deque and __additem__
        reversed_deque += deque[len(deque) - i - 1]

    return reversed_deque  # type: ignore
    # as an aside i have no idea how to fix invariance and python types suck anyways so w/e
