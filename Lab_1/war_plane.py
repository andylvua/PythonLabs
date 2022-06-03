from Lab_1.plane import Plane


class WarPlane(Plane):
    def __init__(self,  max_speed: int, acceleration: int, damaged: bool, max_weigh_of_ammo: int,
                 ammo_equipped: bool, name: str):
        Plane.__init__(self, max_speed, acceleration)
        self.__damaged = damaged
        self.__max_weigh_of_ammo = max_weigh_of_ammo
        self.__ammo_equipped = ammo_equipped
        self.__name = name

    def take_off(self) -> str:
        self.__on_land = False
        return "The warplane has just taken off"

    def land_the_plane(self) -> str:
        if self.__on_land:
            return "The warplane is already on the ground"
        elif not self.__on_land and self.__ammo_equipped:
            print("ammo is not empty, you sure you want to land? (Y/N)")
            answer = input()
            if answer.lower() == "y":
                self.__on_land = True
                return "The warplane landed successfully"
            else:
                return "Ok, continue flying"
        else:
            self.__on_land = True
            return "The warplane landed successfully"

    def check_status(self) -> str:
        if self.__on_land:
            return "The warplane is on the ground, ready to take off"
        else:
            return "The warplane is in air, ready to land"

    def set_damaged(self):
        self.__damaged = True

    def get_name(self):
        return self.__name

    def get_damaged(self):
        return self.__damaged

    def get_ammo_equipped(self):
        return self.__ammo_equipped

    def get_max_weigh_of_ammo(self):
        return self.__max_weigh_of_ammo
