from CivilPlane import CivilPlane


class PassengerPlane(CivilPlane):
    def __init__(self, max_speed: int, acceleration: int, level_of_comfort: str, max_number_of_passengers: int, fuel_consumption_per_km: int, name: str) -> None:
        CivilPlane.__init__(self, max_speed, acceleration, level_of_comfort, name)
        self.__max_number_of_passengers = max_number_of_passengers
        self.__fuel_consumption_per_km = fuel_consumption_per_km

    def take_off(self) -> str:
        self.__on_land = False
        return f"The passenger plane {self.get_name()} has just taken off"

    def land_the_plane(self) -> str:
        if self.__on_land:
            return f"The passenger plane {self.get_name()} is already on the ground, passengers are waiting"
        else:
            self.__on_land = True
            return f"The passenger plane {self.get_name()} landed successfully, every passenger is clapping his hands"

    def check_status(self) -> str:
        if self.__on_land:
            return f"The passenger plane {self.get_name()} is on the ground, ready to take off"
        else:
            return f"The passenger plane {self.get_name()} is in air, ready to land"

    def check_the_comfort_level(self):
        return f"the passenger plane {self.get_name()} has a {self.get_level_of_comfort()} comfort"

    def calculate_the_amount_of_fuel_needed(self, distance_in_km: int):
        fuel = distance_in_km * self.__fuel_consumption_per_km
        return f"the plane {self.get_name()} needs {fuel} liters of fuel"

    def get_max_number_of_passengers(self):
        return self.__max_number_of_passengers

    def get_fuel_consumption_per_km(self):
        return self.__fuel_consumption_per_km
