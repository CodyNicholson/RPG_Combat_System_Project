from battle import Battle
from utils import print_title, choose_ships_for_battle

'''
 - Build
 - Battle
 - Quit
'''

print_title()
endgame = False
while not endgame:
    ships_for_battle = choose_ships_for_battle()
    battle = Battle(ship_list=ships_for_battle)
    battle.start_battle()
