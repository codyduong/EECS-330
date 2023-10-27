class FlightNode:
    def __init__(self, flight_number: int, trip_id: str, passengers: int) -> None:
        self.flight_number = flight_number
        self.trip_id = trip_id
        self.passengers = passengers

    def __repr__(self) -> str:
        return f"Flight {self.flight_number} flying {self.trip_id} with {self.passengers} souls"