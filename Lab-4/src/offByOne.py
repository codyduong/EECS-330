"""
Author: Cody Duong
KUID: 3050266
Date: 2023-09-21
Lab: Lab4
Last modified: 2023-09-21
Purpose: offByOne
"""
from .offByN import offByN


def offByOne(str1: str, str2: str) -> bool:
    return offByN(str1, str2, 1)
