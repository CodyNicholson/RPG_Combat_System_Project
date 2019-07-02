from ship import Ship
from db import save_ship

class Battle:
    def __init__(self, ship_list : list):
        self.ship_list = ship_list
        self.current_ship = ship_list[0]
        self.turn_count = 1
        self.other_ships = []

    def start_game(self) -> None:
        while not self.check_if_game_over():
            self.get_action_order()
            for ship in self.get_ships_not_sunk():
                self.turn_count += 0
                self.current_ship = ship
                self.other_ships = self.get_list_of_other_ships_not_sunk()
                self.start_turn()

    def start_turn(self) -> None:
        self.upkeep_phase() 
        self.main_phase_1()
        self.combat_phase()
        self.main_phase_2()
        self.clean_up_phase()

    def upkeep_phase(self) -> None:
        print(f"<** The {self.current_ship.get_name()} - TURN {str(self.turn_count)} **>\n")
        self.log_stats()

    def main_phase_1(self):
        print(f"<** The {self.current_ship.get_name()} - Main Phase 1 **>\n")

    def combat_phase(self):
        print(f"<** The {self.current_ship.get_name()} - Combat Phase **>\n")
        self.sort_ships_list_on_spd()
        self.select_moves()
        self.log_stats()

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
            ship_action = self.current_ship.choose_action()
            if ship_action == 1:
                self.choose_target()
            elif ship_action == 2:
                self.current_ship.defend()
            elif ship_action == 3:
                self.current_ship.concede()
            else:
                print("Unreachable code!\n")
        self.check_if_game_over()
                
    def choose_target(self) -> None:
        print("<*** CHOOSE TARGET ***>")
        for index, enemy_ship in enumerate(self.other_ships):
            print(f"{index+1} - {enemy_ship.get_name()}")
        chosen_enemy_ship_input = input("> ")
        print()
        if chosen_enemy_ship_input.isdigit():
            chosen_enemy_ship_index = int(chosen_enemy_ship_input) - 1
        else:
            self.choose_target()
            return
        if chosen_enemy_ship_index > (len(self.other_ships)-1) or chosen_enemy_ship_index < 0:
            self.choose_target()
            return
        chosen_ship_name = self.other_ships[chosen_enemy_ship_index].get_name()
        print(f"The {self.current_ship.get_name()} attacked The {chosen_ship_name}\n")
        for ship in self.ship_list:
            if ship.get_name() == chosen_ship_name:
                ship_sunk = ship.take_damage(self.current_ship.get_temp_atk())
                if ship_sunk:
                    self.calc_and_assign_exp(self.current_ship, ship)
                else:
                    self.assign_exp(self.current_ship, 1)

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
            for ship in self.ship_list:
                ship.total_exp()
                save_ship(ship=ship)
                if ship.get_temp_hp() > 0:
                    last_ship = ship
            print(f"Game Over: The {last_ship.get_name()} Wins!\n")
            exit()
        elif len(ships_remaining) < 1:
            print("No one survived. Error?\n")
            return True
        return False

    def assign_exp(self, ship, exp):
        ship.increase_temp_exp(exp)

    def calc_and_assign_exp(self, atk_ship, defeated_ship):
        atk_ship_lvl = atk_ship.get_lvl()
        defeated_ship_lvl = defeated_ship.get_lvl()
        lvl_diff = defeated_ship_lvl - atk_ship_lvl
        calc_exp = 50
        if lvl_diff > 0:
            calc_exp = (75 + (lvl_diff * 25))
        elif lvl_diff < 0:
            calc_exp = (50 + (lvl_diff * 5)) if (lvl_diff > -10) else 0
        atk_ship.increase_temp_exp(calc_exp)
