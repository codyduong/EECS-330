from typing import List


class Sorting:
    def __init__(self, size: int) -> None:
        self.arr: List[int] = []  # Initialize an empty list
        self.size: int = size

    def add(self, element: int) -> None:
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")

    def quicksort(self, low: int = 0, high: int | None = None) -> None:
        if high is None:
            high = len(self.arr) - 1
        if low < high:
            pi: int = self.partition(low, high)  # Partitioning index
            self.quicksort(low, pi - 1)  # Recursively sort elements before partition
            self.quicksort(pi + 1, high)  # Recursively sort elements after partition

    def partition(self, low: int, high: int) -> int:
        """
        Implements in-place partitioning around a pivot.
        Elements less than the pivot are moved to its left, and greater to its right.
        The pivot is chosen using the median_of_three method.
        It is crucial to rearrange the elements within the array itself,
        avoiding the use of additional arrays or significant extra space.
        low : Starting index, high : Ending index
        Returns the partitioning index.
        """
        pivot_index: int = self.median_of_three(low, high)
        pivot_value: int = self.arr[pivot_index]

        # Move pivot to the end
        self.arr[pivot_index], self.arr[high] = self.arr[high], self.arr[pivot_index]

        # Initialize the index to track the smaller elements
        smaller_index: int = low

        # Iterate through the elements in the range [low, high-1]
        for i in range(low, high):
            if self.arr[i] < pivot_value:
                # Swap elements if smaller than the pivot
                self.arr[i], self.arr[smaller_index] = (
                    self.arr[smaller_index],
                    self.arr[i],
                )
                smaller_index += 1

        # Move the pivot to its final position
        self.arr[smaller_index], self.arr[high] = (
            self.arr[high],
            self.arr[smaller_index],
        )

        return smaller_index

    def median_of_three(self, low: int, high: int) -> int:
        """
        Selects the median of the first, middle, and last elements as the pivot.
        This method is used to improve performance by avoiding worst-case scenarios.
        low : Starting index, high : Ending index
        Returns the index of the median element.
        """
        mid: int = (
            low + high
        ) // 2  # choose the first of the two medians on odd len lists
        if (
            self.arr[low] < self.arr[mid] < self.arr[high]
            or self.arr[high] < self.arr[mid] < self.arr[low]
        ):
            return mid
        if (
            self.arr[mid] < self.arr[low] < self.arr[high]
            or self.arr[high] < self.arr[low] < self.arr[mid]
        ):
            return low
        return high
