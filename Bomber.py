from WarPlane import WarPlane


class Bomber(WarPlane):
    def __init__(self, max_speed: int, acceleration: int, damaged: bool, max_weigh_of_ammo: int,
                 ammo_equipped: bool, name: str, nuke_carrier: bool):
        super().__init__(max_speed, acceleration, damaged, max_weigh_of_ammo, ammo_equipped, name)
        self.__nuke_carrier = nuke_carrier

    def take_off(self) -> str:
        self.__on_land = False
        return f"The bomber {self.get_name()} has just taken off"

    def land_the_plane(self) -> str:
        if self.__on_land:
            return f"The bomber {self.get_name()} is already on the ground"
        elif not self.__on_land and self.__ammo_equipped:
            print("ammo is not empty, you sure you want to land? (Y/N)")
            answer = input()
            if answer.lower() == "y":
                self.__on_land = True
                return f"The bomber {self.get_name()} landed successfully"
            else:
                return "Ok, continue flying"
        else:
            self.__on_land = True
            return f"The bomber {self.get_name()} landed successfully"

    def check_status(self) -> str:
        if self.__on_land:
            return f"The bomber {self.get_name()} is on the ground, ready to take off"
        else:
            return f"The bomber {self.get_name()} is in air, ready to land"

    def nuke_putin(self):
        for i in range(0, 10):
            self.__ammo_equipped = False
            print("putin dead ahahhaha")
        return "putin dead successfully"

    def get_nuke_carrier(self):
        return self.__nuke_carrier
