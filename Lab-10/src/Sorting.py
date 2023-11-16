import time
from typing import Literal


class Sorting:
    def __init__(self, size: int) -> None:
        self.arr: list[int] = []  # Initialize an empty list
        self.size: int = size

    def add(self, element: int) -> None:
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")

    def selection_sort(self) -> None:
        """Implements selection sort"""
        for i in range(len(self.arr)):
            min_index: int = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

    def max_heapify(self, n: int, i: int) -> None:
        """Implements Heapify for array"""
        largest: int = i
        left: int = 2 * i + 1
        right: int = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(n, largest)

    def heap_sort(self) -> None:
        """Implements Heap sort"""
        n: int = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.max_heapify(i, 0)

    def merge_sort(self) -> None:
        """Implements Merge sort"""
        if len(self.arr) > 1:
            mid: int = len(self.arr) // 2
            left_half: list[int] = self.arr[:mid]
            right_half: list[int] = self.arr[mid:]

            left_sorter = Sorting(0)
            left_sorter.arr = left_half
            left_sorter.merge_sort()

            right_sorter = Sorting(0)
            right_sorter.arr = right_half
            right_sorter.merge_sort()

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    self.arr[k] = left_half[i]
                    i += 1
                else:
                    self.arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                self.arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                self.arr[k] = right_half[j]
                j += 1
                k += 1

    def test_sorting_time(
        self, sorting_method: Literal["selection", "heap", "merge"]
    ) -> float:
        start_time: float = time.time()
        if sorting_method == "selection":
            self.selection_sort()
        elif sorting_method == "heap":
            self.heap_sort()
        elif sorting_method == "merge":
            self.merge_sort()
        else:
            raise ValueError(
                "Invalid sorting method. Please choose 'selection', 'heap', or 'merge'."
            )
        end_time: float = time.time()
        return end_time - start_time
