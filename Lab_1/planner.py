from civil_plane import CivilPlane


class Planner(CivilPlane):
    def __init__(self, max_speed: int, acceleration: int, level_of_comfort: str, wingspan_in_meters: int,
                 fall_rate_in_meters_per_sec: int, name: str) -> None:
        CivilPlane.__init__(self, max_speed, acceleration, level_of_comfort, name)
        self.__wingspan = wingspan_in_meters
        self.__fall_rate = fall_rate_in_meters_per_sec

    def take_off(self) -> str:
        self.__on_land = False
        return f"The planner {self.get_name()} has just taken off"

    def land_the_plane(self) -> str:
        if self.__on_land:
            return f"The planner {self.get_name()} is already on the ground, passengers are waiting"
        else:
            self.__on_land = True
            return f"The planner {self.get_name()} landed successfully, every passenger is clapping his hands"

    def check_status(self) -> str:
        if self.__on_land:
            return f"The planner {self.get_name()} is on the ground, ready to take off"
        else:
            return f"The planner {self.get_name()} is in air, ready to land"

    def check_the_comfort_level(self):
        return f"the planner {self.get_name()} has a {self.get_level_of_comfort()} comfort"

    def calculate_the_maximum_flight_distance(self, starting_height: int):
        distance = self.get_max_speed() * starting_height/self.get_fall_rate()/1000
        return f"the planner {self.get_name()} can fly {distance} km on its maximum"

    def get_fall_rate(self):
        return self.__fall_rate

    def get_wingspan(self):
        return self.__wingspan
