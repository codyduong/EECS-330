from typing import Any, Generic, Optional, Tuple, TypeVar, Union, cast

from src.FlightNode import FlightNode

HashMapValue = TypeVar("HashMapValue", bound="Any")

class HashMap(Generic[HashMapValue]):
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.hash_table: list[list[tuple[Union[str, int], HashMapValue]]] = [[] for _ in range(size)]
        self.num_elements = 0
        self.load_factor = 1.5

    def _hash_function(self, key: Union[str, int]) -> int:
        return hash(key) % self.size
    
    def _resize(self, new_size: int) -> None:
        # Create a new, larger hash table and rehash all elements
        new_table: list[list[Any]] = [[] for _ in range(new_size)]
        for bucket in self.hash_table:
            for key, value in bucket:
                new_index: int = self._hash_function(key)
                new_table[new_index].append((key, value))
        self.hash_table = new_table
        self.size = new_size

    def put(self, key: Union[str, int], value: HashMapValue) -> None:
        """Insert or update a key-value pair in the hash map."""
        index: int = self._hash_function(key)
        self.hash_table[index].append((key, value))
        self.num_elements += 1
        if self.num_elements / self.size >= self.load_factor:
            # If the load factor is exceeded, resize the hash table to double
            new_size: int = self.size * 2
            self._resize(new_size)

    def get(self, key: Union[str, int]) -> Optional[HashMapValue]:
        """Get the value associated with a key from the hash map."""
        index: int = self._hash_function(key)
        for k, v in self.hash_table[index]:
            if k == key:
                return v
        return None

    def remove(self, key: Union[str, int], value: HashMapValue) -> None:
        """Remove a key-value pair from the hash map."""
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self.hash_table[index]):
            if k == key and v == value:
                del self.hash_table[index][i]
                return

    def display(self) -> list[list[Any]]:
        """Display the updated hash map."""
        return self.hash_table
    
    def max_passengers_in_flight(self, flight_number: int) -> Optional[int]:
        """Find the trip with the largest number of passengers on the specified flight."""
        max_passengers_trip: tuple[str, int] = ("", 0)
        index: int = self._hash_function(flight_number)
        # print(self.hash_table[index])
        for trip_id, flightnode in cast(list[Tuple[str, FlightNode]], self.hash_table[index]):
            # double check same flight number
            if flightnode.passengers > max_passengers_trip[1] and flightnode.flight_number == flight_number:
                max_passengers_trip = (trip_id, flightnode.passengers)
        if max_passengers_trip[0] != "":
            return max_passengers_trip[1]
        else:
            return None