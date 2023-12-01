from random import randint, seed
from typing import List

from src.RadixSort import radix_sort
from src.Sorting import Sorting


def is_sorted(arr: List[int]) -> str:
    if arr == sorted(arr):
        return "Passed!"
    else:
        return "Failed!"


def test_quicksort() -> None:
    """Test the Quicksort algorithm"""
    seed_num = 43
    seed(seed_num)  # Set the seed for reproducibility
    sorting = Sorting(10)
    for _ in range(10):
        sorting.add(randint(1, 100))

    sorting.quicksort(0, len(sorting.arr) - 1)  # Apply the Quicksort algorithm
    print("Quick Sort:", is_sorted(sorting.arr))

def test_radix_sort() -> None:
    # Test case 1
    arr1: List[int] = [234, 34, 34, 2, 1, 0, 2, 3422]
    radix_sort(arr1)
    assert arr1 == [0, 1, 2, 2, 34, 34, 234, 3422], f"Test case 1 failed: {arr1}"

    # Test case 2
    arr2: List[int] = [329, 457, 657, 839, 436, 720, 355]
    radix_sort(arr2)
    assert arr2 == [329, 355, 436, 457, 657, 720, 839], f"Test case 2 failed: {arr2}"

    # Test case 3
    arr3: List[int] = [1, 200, 3, 400, 5]
    radix_sort(arr3)
    assert arr3 == [1, 3, 5, 200, 400], f"Test case 3 failed: {arr3}"

    # Test case 4 (empty array)
    arr4: List[int] = []
    radix_sort(arr4)
    assert arr4 == [], f"Test case 4 failed: {arr4}"

    # Test case 5 (array with one element)
    arr5: List[int] = [42]
    radix_sort(arr5)
    assert arr5 == [42], f"Test case 5 failed: {arr5}"

    # print("All test cases passed!")
    print("Radix sort: Passed!")

# Test case execution
test_quicksort()
# Run the test cases
test_radix_sort()
