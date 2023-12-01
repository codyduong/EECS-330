from typing import List


def counting_sort(arr: List[int], exp: int) -> None:
    n: int = len(arr)
    output: list[int] = [0] * n
    count: list[int] = [0] * 10

    # Count occurrences of each digit.
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update count to store the position of the next occurrence.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array.
    i: int = n - 1
    while i >= 0:
        index: int = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[] to update the original array.
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr: List[int]) -> None:
    # Return if array is empty.
    if not arr:
        return

    # Find the maximum number to know the number of digits.
    max_num: int = max(arr)

    # Do counting sort for every digit.
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

