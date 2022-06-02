from Lab_1.civil_plane import CivilPlane


class SportPlane(CivilPlane):
    def __init__(self, max_speed: int, acceleration: int, level_of_comfort: str,
                 mass_in_kg: int, maneuverability_from_one_to_three: int, name: str) -> None:
        CivilPlane.__init__(self, max_speed, acceleration, level_of_comfort, name)
        self.__mass_in_kg = mass_in_kg
        self.__maneuverability = maneuverability_from_one_to_three

    def take_off(self) -> str:
        self.__on_land = False
        return f"The sport plane {self.get_name()} has just taken off"

    def land_the_plane(self) -> str:
        if self.__on_land:
            return f"The sport plane {self.get_name()} is already on the ground, passengers are waiting"
        else:
            self.__on_land = True
            return f"The sport plane {self.get_name()} landed successfully, every passenger is clapping his hands"

    def check_status(self) -> str:
        if self.__on_land:
            return f"The sport plane {self.get_name()} is on the ground, ready to take off"
        else:
            return f"The sport plane {self.get_name()} is in air, ready to land"

    def check_the_comfort_level(self):
        return f"the sport plane {self.get_name()} has a {self.__level_of_comfort} comfort"

    def do_maneuver(self):
        print("which maneuver you want to do?:\nbarrel, cuban eight or dead loop")
        decision = input()
        if decision == "barrel":
            return "You`ve done a great barrel roll"
        elif decision == "dead loop":
            if self.__maneuverability >= 2:
                return "That was a great loop"
            else:
                return "You can`t do that, your plane will crash, it is not suitable for this"
        elif decision == "cuban eight":
            if self.__maneuverability == 3:
                return "What a beautiful trick, very good"
            else:
                return "You can`t do that, your plane will crash, it is not suitable for this"
        else:
            return "There`s no such trick like this"

    def get_mass_in_kg(self):
        return self.__mass_in_kg

    def get_maneuverability(self):
        return self.__maneuverability
