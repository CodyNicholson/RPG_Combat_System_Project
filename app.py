from ship import Ship
from battle import Battle
from utils import print_title
from db import create_ship, create_ship_list

# Create a battle object that takes the list of ships and starts the battle
print_title()
ship_list = create_ship_list()
battle = Battle(ship_list=ship_list)
battle.start_turn()
