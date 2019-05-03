from ship import Ship

class Battle:
    def __init__(self, ship_list : list):
        self.ship_list = ship_list
        self.defeated_ships_list = []
        self.turn_count = 0

    def start_turn(self):
        self.upkeep_phase() 
        self.main_phase_1()
        self.combat_phase()
        self.main_phase_2()
        self.clean_up_phase()
        self.start_turn()

    def upkeep_phase(self) -> None:
        if len(self.ship_list) > 1:
            pass
        else:
            print(f"Game Over: The {self.ship_list[0].get_name()} Wins!\n")
            exit()
        self.turn_count += 1
        print(f"\n<****** TURN {str(self.turn_count)} ******>")
        self.log_stats()

    def main_phase_1(self):
        pass

    def combat_phase(self):
        self.sort_ships_list_on_spd()
        print(f"**** ACTION ORDER ****")
        for index, ship in enumerate(self.ship_list):
            print(f"{index+1} - {ship.get_name()} ({ship.get_spd()} spd)")
        self.select_moves()
        self.log_stats()

    def main_phase_2(self):
        pass

    def clean_up_phase(self):
        pass
        
    def sort_ships_list_on_spd(self) -> None:
        self.ship_list.sort(key=lambda ship: ship.get_spd(), reverse=True)

    def select_moves(self):
        print("\n*** SELECT ACTIONS ***")
        for current_ship in self.ship_list:
            ship_action = current_ship.choose_action()
            if ship_action == 1:
                chosen_ship_index = self.choose_target(current_ship)
                
    def choose_target(self, current_ship : Ship) -> None:
        print("*** CHOOSE TARGET ***")
        other_ships = self.get_list_of_other_ships(current_ship)
        for index, enemy_ship in enumerate(other_ships):
            print(f"{index+1} - {enemy_ship.get_name()}")
        chosen_enemy_ship_input = input("> ")
        if chosen_enemy_ship_input.isdigit():
            chosen_enemy_ship_index = int(chosen_enemy_ship_input) - 1
        else:
            self.choose_target(current_ship)
            return
        if chosen_enemy_ship_index > (len(other_ships)-1) or chosen_enemy_ship_index < 0:
            self.choose_target(current_ship)
            return
        chosen_ship_name = other_ships[chosen_enemy_ship_index].get_name()
        print(f"The {current_ship.get_name()} attacked The {chosen_ship_name}\n")
        for ship in self.ship_list:
            if ship.get_name() == chosen_ship_name:
                destroyed = ship.take_damage(current_ship.get_atk())
                if destroyed:
                    self.remove_ship_by_name(ship.get_name())
                return

    def get_list_of_other_ships(self, current_ship : Ship) -> list:
        other_ships = []
        for ship in self.ship_list:
            if ship != current_ship:
                other_ships.append(ship)
        return other_ships

    def log_stats(self):
        print("\n***** BATTLE LOG *****")
        for ship in self.ship_list:
            print(f"{ship.get_name()} has {ship.get_r_hp()} hp")
        print("")

    def remove_ship_by_name(self, ship_name):
        for ship in self.ship_list:
            if ship.get_name() == ship_name:
                self.ship_list.remove(ship)
                