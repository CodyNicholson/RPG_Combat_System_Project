from character import Character

class Battle:
    def __init__(self, char_list : list):
        self.char_list = char_list
        self.defeated_chars_list = []
        self.turn_count = 0

    def start_turn(self):
        self.turn_count += 1
        print(f"\n<****** TURN {str(self.turn_count)} ******>\n")
        self.sort_chars_list_on_spd()
        print(f"**** ACTION ORDER ****")
        for i in self.char_list:
            print(f"{i.get_name()} has {i.get_spd()} spd")
        self.log_stats()
        if len(self.char_list) > 1:
            print(f"*** SELECT ACTIONS ***")
            self.select_moves()
        else:
            return
        
    def sort_chars_list_on_spd(self) -> None:
        self.char_list.sort(key=lambda char: char.get_spd(), reverse=True)

    def select_moves(self):
        for character in self.char_list:
            character.choose_action()

    def log_stats(self):
        print("\n***** BATTLE LOG *****")
        for character in self.char_list:
            print(f"{character.get_name()} has {character.get_hp()} hp")
        print("")

    # def are_more_than_one_player_alive(self) -> bool:
    #     players_alive = 0
    #     for character in self.char_list:
    #         if character.get_hp() > 0:
    #             players_alive += 1
    #     if players_alive > 1:
    #         print("The fight continues!\n")
    #         return True
    #     else:
    #         print("Game over!\n")
    #         return False
