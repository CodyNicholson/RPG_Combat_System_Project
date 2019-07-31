from build import choose_build
from battle import choose_battle
from utils import print_title

print_title()
endgame = False
while not endgame:
    print("Main Menu:\n1 - Build\n2 - Battle\n3 - Quit")
    try:
        main_menu_selection = int(input("> "))
        print()
        if main_menu_selection == 1:
            choose_build()
        elif main_menu_selection == 2:
            choose_battle()
        elif main_menu_selection == 3:
            print("bye\n")
            endgame = True
    except Exception:
        print("\nInvalid input\n")
