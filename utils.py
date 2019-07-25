from db import create_ship_list

def print_title():
    print("""\
        ____ ___  ____    ____ ____ _  _ ___  ____ ___    ____ _   _ ____ ___ ____ _  _    ___  ____ ____  _ ____ ____ ___ 
        |__/ |__] | __    |    |  | |\/| |__] |__|  |     [__   \_/  |___  |  |___ |\/|    |__] |__/ |  |  | |___ |     |  
        |  \ |    |__]    |___ |__| |  | |__] |  |  |     ___]   |   |___  |  |___ |  |    |    |  \ |__| _| |___ |___  |  
    """)

def choose_ships_for_battle():
    all_ships = create_ship_list()
    ships_for_battle = []
    keep_going = True
    while keep_going:
        print("Select battleships:\n0 - Finish Selecting")
        for index, ship in enumerate(all_ships):
            print(f"{index+1} - {ship.get_name()}")
        ship_index = input("> ")
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
            print("Ships in battle so far:")
            for s in ships_for_battle:
                print(s.get_name())
        print()
    return ships_for_battle
