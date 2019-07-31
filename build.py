from db import get_ships, create_ship, delete_ship

def choose_build():
    keep_going = True
    while keep_going:
        print("Build Menu:\n0 - Go Back\n1 - Create Battleship\n2 - Modify Battleship\n3 - Delete Battleship")
        try:
            selection = int(input("> "))
            if selection == 0:
                keep_going = False
            elif selection == 1:
                name = choose_name()
                if name == "0" or name == "":
                    print()
                    continue
                typ = choose_type()
                if typ == "":
                    print()
                    continue
                create_ship(name=name, typ=typ)
            elif selection == 2:
                modify_ships()
            elif selection == 3:
                delete_battleship()
        except Exception:
            print("\nInvalid input\n")
        print()

def delete_battleship() -> None:
    all_ships = get_ships()
    keep_going = True
    while keep_going:
        print("\nDelete Which Ship?\n0 - Go Back")
        for index, ship in enumerate(all_ships):
            print(f"{index+1} - {ship.get_name()} - Lvl {ship.get_lvl()} {ship.get_typ()}")
        try:
            delete_index = int(input("> "))
            if delete_index > 0 and delete_index <= len(all_ships):
                print(f"\nDELETE: The {all_ships[delete_index-1].get_name()}")
                delete_ship(name=all_ships[delete_index-1].get_name())
                keep_going = False
            elif delete_index == 0:
                keep_going = False
            else:
                print("\nInvalid Input")
        except Exception:
            print("\nInvalid Input")

def choose_name() -> str:
    existing_names = get_all_ship_names()
    while True:
        print("\nEnter Ship Name:\n0 - Go Back")
        ship_name_input = input("> ")
        if ship_name_input.lower() in existing_names:
            print("\nName already taken")
        else:
            return ship_name_input

def get_all_ship_names() -> list:
    names = []
    all_ships = get_ships()
    for ship in all_ships:
        names.append(ship.get_name().lower())
    return names

def choose_type() -> str:
    while True:
        print("\nSelect Ship Type:\n0 - Go Back\n1 - Cruiser\n2 - Glider\n3 - Bomber")
        try:
            user_type_input = int(input("> "))
            if user_type_input == 0:
                return ""
            elif user_type_input == 1:
                return "Crusier"
            elif user_type_input == 2:
                return "Glider"
            elif user_type_input == 3:
                return "Bomber"
        except Exception:
            print("\nInvalid Input\n")

def modify_ships():
    all_ships = get_ships()
    print("\nShips in harbor:")
    for ship in all_ships:
        print(f" - The {ship.get_name()} - Lvl {ship.get_lvl()} {ship.get_typ()}")
