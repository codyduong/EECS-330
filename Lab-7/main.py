# Display the hash map
from typing import Union
from src.FlightNode import FlightNode
from src.Hashmap import HashMap

my_hash_map = HashMap[int](7)
# 0, 1, 4, 9, 16, 25, 36, 49, 64, 81
my_hash_map.put("aaa", 0)
my_hash_map.put("bbb", 1)
my_hash_map.put("ccc", 4)
my_hash_map.put("ddd", 9)
my_hash_map.put("eee", 16)
my_hash_map.put("fff", 25)
my_hash_map.put("ggg", 36)
my_hash_map.put("hhh", 49)
my_hash_map.put("ccc", 64)
my_hash_map.put("ccc", 81)
print(my_hash_map.display())

# Retrieve values
print("Retrieve values:")
print("aaa:", my_hash_map.get("aaa"))  
print("bbb:", my_hash_map.get("bbb"))
print("ccc:", my_hash_map.get("ccc"))

# Remove a key-value pair
my_hash_map.remove("bbb", 1)  

# Display the updated hash map
print(my_hash_map.display())

#Max Passengers on Trip
my_map = HashMap[FlightNode](11)

my_map.put(16, FlightNode(16, "Trip 1", 300))
my_map.put(16, FlightNode(16, "Trip 2", 700))
my_map.put(29, FlightNode(29, "Trip 1", 800))
my_map.put(29, FlightNode(29, "Trip 2", 250))
my_map.put(36, FlightNode(29, "Trip 3", 500))
my_map.put(36, FlightNode(36, "Trip 1", 500))
my_map.put(36, FlightNode(36, "Trip 2", 340))
my_map.put(36, FlightNode(36, "Trip 3", 900))
my_map.put(36, FlightNode(36, "Trip 4", 400))
my_map.put(49, FlightNode(49, "Trip 1", 250))
my_map.put(49, FlightNode(49, "Trip 2", 550))
# print(my_map.display())

max_passengers: Union[int, None] = my_map.max_passengers_in_flight(49)
if max_passengers is not None:
    print("Largest number of people in flight at once :", max_passengers)
else:
    print("Flight not found in the map")