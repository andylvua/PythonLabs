from Bomber import Bomber
from Destroyer import Destroyer
from PassengerPlane import PassengerPlane
from Planner import Planner
from SportPlane import SportPlane


def main():
    bomber = Bomber(1200, 5, False, 5000, True, "PUTIN DESTROYER", True)
    bomber_putin = Bomber(12, -999, False, 0, True, "putins plane", True)
    destroyer = Destroyer(2500, 25, False, 200, True, "Ghost of Kyiv", 5)
    passenger_plane = PassengerPlane(800, 10, "high", 400, 1, "Dora")
    planner = Planner(150, 0, "low", 9, 1, "slider")
    sport_plane = SportPlane(400, 18, "medium", 400, 1, "RedBull")

    print(destroyer.take_off())
    print(destroyer.check_status())
    print(destroyer.attack_enemy_bomber(bomber_putin))
    print(destroyer.get_destroyed_targets())
    print(passenger_plane.calculate_the_amount_of_fuel_needed(20000))
    print(passenger_plane.check_the_comfort_level())
    print(planner.calculate_the_maximum_flight_distance(9000))
    print(sport_plane.do_maneuver())
    print(destroyer.land_the_plane())
    print(bomber.nuke_putin())


if __name__ == '__main__':
    main()
