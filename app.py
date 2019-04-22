from character import Character
from battle import Battle

# Print title
print("""\
    ____ ___  ____    ____ ____ _  _ ___  ____ ___    ____ _   _ ____ ___ ____ _  _    ___  ____ ____  _ ____ ____ ___ 
    |__/ |__] | __    |    |  | |\/| |__] |__|  |     [__   \_/  |___  |  |___ |\/|    |__] |__/ |  |  | |___ |     |  
    |  \ |    |__]    |___ |__| |  | |__] |  |  |     ___]   |   |___  |  |___ |  |    |    |  \ |__| _| |___ |___  |  
""")

# Create characters for combat
char1 = Character(name="Char1", atr="fire", hp=100, atk=15, res=10, spd=6)
char2 = Character(name="Char2", atr="water", hp=150, atk=10, res=15, spd=8)
char3 = Character(name="Char3", atr="dark", hp=150, atk=10, res=15, spd=7)

# Put those characters into a single object
char_list = [char1, char2, char3]

# Create a battle object that takes the list of characters and start the battle
battle = Battle(char_list=char_list)
battle.start_turn()
