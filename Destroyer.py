from Bomber import Bomber
from WarPlane import WarPlane


class Destroyer(WarPlane):
    def __init__(self, max_speed: int, acceleration: int, damaged: bool, max_weigh_of_ammo: int, ammo_equipped: bool, name: str, generation: int):
        super().__init__(max_speed, acceleration, damaged, max_weigh_of_ammo, ammo_equipped, name)
        self.__number_of_destroyed_planes = 0
        self.__generation = generation

    def take_off(self) -> str:
        self.__on_land = False
        return f"The destroyer {self.get_name()} has just taken off"

    def land_the_plane(self) -> str:
        if self.__on_land:
            return f"The destroyer {self.get_name()} is already on the ground"
        elif not self.__on_land and self.__ammo_equipped:
            print("ammo is not empty, you sure you want to land? (Y/N)")
            answer = input()
            if answer.lower() == "y":
                self.__on_land = True
                return f"The destroyer {self.get_name()} landed successfully"
            else:
                return "Ok, continue flying"
        else:
            self.__on_land = True
            return f"The destroyer {self.get_name()} landed successfully"

    def check_status(self) -> str:
        if self.__on_land:
            return f"The destroyer {self.get_name()} is on the ground, ready to take off"
        else:
            return f"The destroyer {self.get_name()} is in air, ready to land"

    def attack_enemy_bomber(self, bomber: Bomber):
        bomber.set_damaged = True
        self.__ammo_equipped = False
        self.__number_of_destroyed_planes += 1
        return "bomber destroyed successfully"

    def get_destroyed_targets(self):
        return f"You`ve destroyed {self.get_number_of_destroyed_planes()} planes"

    def get_number_of_destroyed_planes(self):
        return self.__number_of_destroyed_planes

    def get_generation(self):
        return self.__generation
