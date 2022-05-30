class Plane:
    def __init__(self, max_speed: int, acceleration: int):
        self.__max_speed = max_speed
        self.__acceleration = acceleration
        self.__on_land = True

    def take_off(self) -> str:
        self.__on_land = False
        return "The plane has just taken off"

    def land_the_plane(self) -> str:
        if self.__on_land:
            return "The plane is already on the ground"
        else:
            self.__on_land = True
            return "The plane landed successfully"

    def check_status(self) -> str:
        if self.__on_land:
            return "The plane is on the ground, ready to take off"
        else:
            return "The plane is in air, ready to land"

    def get_max_speed(self):
        return self.__max_speed

    def get_acceleration(self):
        return self.__acceleration

    def get_on_land(self):
        return self.__on_land
