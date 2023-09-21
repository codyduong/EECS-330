"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-21
Lab: Lab4
Last modified: 2023-09-21
Purpose: offByN
"""
from .DLList import DLList


LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ASCII_DEQUE = DLList.Deque[str](*LETTERS)


def offByN(str1: str, str2: str, n: int) -> bool:
    """
    Compare how off two strings are off from each other by using deque

    :param str1:
    :param str2:
    :param N: number of characters off by
    :return: bool
    """
    # there is some class type hierarchy issues which results in unknown T type, w/e
    str1_index: int = ASCII_DEQUE.find(str1)  # type: ignore
    str2_index: int = ASCII_DEQUE.find(str2)  # type: ignore
    if str1_index != -1 and str2_index != -1:
        if str1_index > str2_index:
            return (str1_index - str2_index) == n
        else:
            return (str2_index - str1_index) == n

    return False
