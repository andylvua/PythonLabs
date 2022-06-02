from plane import Plane


class CivilPlane(Plane):
    def __init__(self,  max_speed: int, acceleration: int, level_of_comfort: str, name: str) -> None:
        Plane.__init__(self, max_speed, acceleration)
        self.__level_of_comfort = level_of_comfort
        self.__name = name

    def take_off(self) -> str:
        self.__on_land = False
        return "The civil plane has just taken off"

    def land_the_plane(self) -> str:
        if self.__on_land:
            return "The civil plane is already on the ground"
        else:
            self.__on_land = True
            return "The civil plane landed successfully"

    def check_status(self) -> str:
        if self.__on_land:
            return "The civil plane is on the ground, ready to take off"
        else:
            return "The civil plane is in air, ready to land"

    def check_the_comfort_level(self):
        return f"the plane has a {self.get_level_of_comfort()} comfort"

    def get_name(self):
        return self.__name

    def get_level_of_comfort(self):
        return self.__level_of_comfort
