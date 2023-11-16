# Test Sorted array
from random import randint, seed
from typing import Literal
from src.Sorting import Sorting


def is_sorted(arr: list[int]) -> str:
    if arr == sorted(arr):
        return "Passed!"
    else:
        return "Failed!"


# Test each sirting technique
def test_sort_algorithms(
    sorting_method: Literal["selection", "heap", "merge"],
    set_seed: int | float | str | bytes | bytearray | None = None,
) -> None:
    if set_seed != None:
        seed(set_seed)
    sorting = Sorting(10)
    # Add 10 random elements
    for _ in range(10):
        sorting.add(randint(1, 100))
    # Apply the sorting algorithm
    if sorting_method == "selection":
        sorting.selection_sort()
        print("Selection Sort:", is_sorted(sorting.arr))
    elif sorting_method == "heap":
        sorting.heap_sort()
        print("Heap Sort:", is_sorted(sorting.arr))
    elif sorting_method == "merge":
        sorting.merge_sort()
        print("Merge Sort:", is_sorted(sorting.arr))


# Test run time
def run_time_tests() -> None:
    seeding = 45
    array_sizes: list[int] = [10000, 20000, 30000, 40000, 50000]
    methods: list[Literal["selection", "heap", "merge"]] = [
        "selection",
        "heap",
        "merge",
    ]
    print("Array Size\t\tSelection Sort\t\tHeap Sort\t\tMerge Sort")
    for size in array_sizes:
        times: list[float] = []
        for m in methods:
            sorting = Sorting(size)
            seed(seeding)
            for _ in range(size):
                sorting.add(randint(1, 50000))
            interval: float = sorting.test_sorting_time(m)
            times.append(interval)
        print(f"{size}\t\t{times[0]:.6f}\t\t{times[1]:.6f}\t\t{times[2]:.6f}")


# test case execution
seed_num = 43
test_sort_algorithms("selection", seed_num)
test_sort_algorithms("heap", seed_num)
test_sort_algorithms("merge", seed_num)
run_time_tests()
