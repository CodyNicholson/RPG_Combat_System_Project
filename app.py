from ship import Ship
from battle import Battle
from utils import print_title
from db import create_ship, create_ship_list, save_ship

print_title()
ships = create_ship_list()
battle = Battle(ship_list=ships)
battle.start_battle()
