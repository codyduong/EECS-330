"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-14
Last modified: 2023-09-14
Purpose: isPalindrome
"""

from .DLList import DLList


def isPalindrome(s: str) -> bool:
    # Initialize Deque using Deque class.
    deque = DLList.Deque[str]()
    for char in s:
        deque.append(char)  # type: ignore

    while not deque.empty():
        # check if front and back are equal
        if deque.front() == deque.back():
            try:
                deque.pop()
                deque.pop_front()
            except IndexError:
                # ignore IndexError, it just means we had an odd amount and tried to pop an already empty queue
                pass
        else:
            return False

    return True
