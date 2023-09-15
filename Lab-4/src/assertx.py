"""
Author: Cody Duong
KUID: 3050266
Date: 2022-09-22
Lab: Lab4
Last modified: 2023-09-14
Purpose: Assert extension, send out other error types (rather than just AssertionError)
"""

from typing import Callable, NoReturn, Type, Union


def assertx(
    predicate: Union[Callable[[], bool], bool],
    e: Type[Exception],
    msg: str = str(Exception),
) -> Union[None, NoReturn]:
    """
    Assert extension, checks a predicate or boolean value, and runs the error if true

    :param predicate: A boolean or predicate function which will assert truthiness
    :param e: Exception to raise if predicate is false
    :param msg: Message to send on failure
    """
    if isinstance(predicate, bool):
        if not predicate:
            raise e(msg)
        return None

    if callable(predicate):
        if not predicate():
            raise e(msg)
        return None
