from ship import Ship
from db import save_ship, create_ship_list
import random

class Battle:
    def __init__(self, ship_list : list):
        self.ship_list = ship_list
        self.current_ship = ship_list[0]
        self.turn_count = 0
        self.other_ships = []

    def start_battle(self) -> None:
        while not self.check_if_game_over():
            self.sort_ships_list_on_spd()
            self.get_action_order()
            self.turn_count += 1
            for ship in self.get_ships_not_sunk():
                self.current_ship = ship
                self.other_ships = self.get_list_of_other_ships_not_sunk()
                if not self.current_ship.sunk():
                    self.start_turn()
            print(f"<-- END TURN {self.turn_count} -->\n")

    def start_turn(self) -> None:
        self.upkeep_phase() 
        self.main_phase_1()
        self.combat_phase()
        self.main_phase_2()
        self.clean_up_phase()

    def upkeep_phase(self) -> None:
        print(f"<** The {self.current_ship.get_name()} - TURN {self.turn_count} **>\n")
        self.log_stats()

    def main_phase_1(self):
        print(f"<** The {self.current_ship.get_name()} - Main Phase 1 **>\n")

    def combat_phase(self):
        print(f"<** The {self.current_ship.get_name()} - Combat Phase **>\n")
        self.select_moves()

    def main_phase_2(self):
        print(f"<** The {self.current_ship.get_name()} - Main Phase 2 **>\n")

    def clean_up_phase(self):
        print(f"<** The {self.current_ship.get_name()} - Clean Up Phase **>\n")
        
    def sort_ships_list_on_spd(self) -> None:
        self.ship_list.sort(key=lambda ship: ship.get_temp_spd(), reverse=True)

    def select_moves(self):
        print("<** SELECT ACTION **>")
        if self.current_ship.sunk():
            print("\nThis ship is sunk\n")
        else:
            action_type = self.current_ship.choose_action()
            if action_type == 1:
                self.choose_target(action_type)
            elif action_type == 2:
                self.choose_target(action_type)
            elif action_type == 3:
                self.choose_target(action_type)
            elif action_type == 4:
                self.current_ship.concede()
            else:
                print("Unreachable code!\n")
        self.check_if_game_over()
                
    def choose_target(self, action_type : int) -> None:
        keep_going = True
        while keep_going:
            print("<*** CHOOSE TARGET ***>")
            for index, enemy_ship in enumerate(self.other_ships):
                print(f"{index+1} - {enemy_ship.get_name()}")
            try:
                chosen_enemy_ship_index = int(input("> ")) - 1
                print()
                if chosen_enemy_ship_index < len(self.other_ships) and chosen_enemy_ship_index >= 0:
                    chosen_ship = self.other_ships[chosen_enemy_ship_index]
                    self.calc_ship_attack(chosen_ship, action_type)
                    keep_going = False
            except Exception:
                pass

    def calc_ship_attack(self, chosen_ship : Ship, action_type : int) -> None:
        weapon_txt = "cannons"
        if action_type == 2:
            weapon_txt = "bombs"
        elif action_type == 3:
            weapon_txt = "torpedos"
        print(f"The {self.current_ship.get_name()} attacked The {chosen_ship.get_name()} using the {weapon_txt}\n")
        atk_spd = self.current_ship.get_temp_spd()
        def_spd = chosen_ship.get_temp_spd()
        ship_sunk = False
        if def_spd > (atk_spd * 2):
            hit_chance = 50
            print(f"HC: {hit_chance}\n")
            if random.randint(0,100) < hit_chance:
                ship_sunk = chosen_ship.take_damage(self.current_ship.get_temp_atk())
            else:
                print(f"The {self.current_ship.get_name()} missed The {chosen_ship.get_name()}\n")
        elif def_spd > atk_spd:
            hit_chance = (100 - round(((def_spd-atk_spd)/atk_spd)/2*100))
            print(f"HC: {hit_chance}\n")
            if random.randint(0,100) < hit_chance:
                ship_sunk = chosen_ship.take_damage(self.current_ship.get_temp_atk())
            else:
                print(f"The {self.current_ship.get_name()} missed The {chosen_ship.get_name()}\n")
        else:
            hit_chance = 95
            print(f"HC: {hit_chance}\n")
            if random.randint(0,100) < hit_chance:
                ship_sunk = chosen_ship.take_damage(self.current_ship.get_temp_atk())
            else:
                print(f"The {self.current_ship.get_name()} missed The {chosen_ship.get_name()}\n")
        if ship_sunk:
            self.calc_and_assign_exp(self.current_ship, chosen_ship)
        else:
            self.current_ship.increase_temp_exp(1)

    def get_list_of_other_ships_not_sunk(self) -> list:
        other_ships = []
        for ship in self.ship_list:
            if (ship != self.current_ship) and (ship.get_temp_hp() > 0):
                other_ships.append(ship)
        return other_ships

    def log_stats(self):
        print("<**** BATTLE LOG ****>")
        for ship in self.get_ships_not_sunk():
            print(f"{ship.get_name()} has {ship.get_temp_hp()} hp")
        print()

    def get_ships_not_sunk(self) -> list:
        ships_not_sunk = []
        for ship in self.ship_list:
            if ship.get_temp_hp() > 0:
                ships_not_sunk.append(ship)
        return ships_not_sunk

    def get_action_order(self) -> None:
        print(f"<**** ACTION ORDER ****>")
        for index, ship in enumerate(self.get_ships_not_sunk()):
            print(f"{index+1} - {ship.get_name()} ({ship.get_temp_spd()} spd)")
        print()

    def check_if_game_over(self) -> bool:
        ships_remaining = []
        for ship in self.ship_list:
            if not ship.sunk():
                ships_remaining.append(ship)
        if len(ships_remaining) == 1:
            print("<$$$ EXP Gains $$$>")
            for ship in self.ship_list:
                ship.total_exp()
                save_ship(ship=ship)
                if ship.get_temp_hp() > 0:
                    last_ship = ship
            print(f"\nGame Over: The {last_ship.get_name()} Wins!\n")
            return True
        elif len(ships_remaining) < 1:
            print("<$$$ EXP Gains $$$>")
            for ship in self.ship_list:
                ship.total_exp()
                save_ship(ship=ship)
                if ship.get_temp_hp() > 0:
                    last_ship = ship
            print("No one survived.\n")
            return True
        return False

    def calc_and_assign_exp(self, atk_ship, defeated_ship):
        atk_ship_lvl = atk_ship.get_lvl()
        defeated_ship_lvl = defeated_ship.get_lvl()
        lvl_diff = defeated_ship_lvl - atk_ship_lvl
        calc_exp = 50
        if lvl_diff > 0:
            calc_exp = (50 + (lvl_diff * 25))
        elif lvl_diff < 0:
            calc_exp = (50 + (lvl_diff * 5)) if (lvl_diff > -10) else 0
        atk_ship.increase_temp_exp(calc_exp)

def choose_ships_for_battle():
    all_ships = create_ship_list()
    ships_for_battle = []
    keep_going = True
    while keep_going:
        print("Select Battleships For Battle:\n0 - Finish Selecting")
        for index, ship in enumerate(all_ships):
            print(f"{index+1} - The {ship.get_name()} - Lvl {ship.get_lvl()} {ship.get_typ()}")
        ship_index = input("> ") # REFACTOR
        print()
        if ship_index.isdigit() and int(ship_index) < (len(all_ships)+1) and int(ship_index) > 0:
            ships_for_battle.append(all_ships[int(ship_index) - 1])
            all_ships.remove(all_ships[int(ship_index) - 1])
        elif ship_index.isdigit() and int(ship_index) == 0:
            if len(ships_for_battle) < 2:
                print("There are not enough ships to start a battle")
            else:
                keep_going = False
        if len(ships_for_battle) > 0:
            print("\nShips in battle so far:")
            for s in ships_for_battle:
                print(f" - The {s.get_name()} - Lvl {s.get_lvl()} {s.get_typ()}")
        print()
    return ships_for_battle

def choose_battle():
    ships_for_battle = choose_ships_for_battle()
    battle = Battle(ship_list=ships_for_battle)
    battle.start_battle()
