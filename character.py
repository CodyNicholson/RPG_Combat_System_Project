
class Character:
    def __init__(self, name : str, atr : str, hp : int, atk : int, res : int, spd: int):
        self.name = name
        self.atr = atr
        self.lvl = 1
        self.exp = 0
        self.hp = hp
        self.atk = atk
        self.res = res
        self.spd = spd
        print(f"New character: name = {self.name}, lvl = {self.lvl}, exp = {self.exp}, atr = {self.atr}, hp = {self.hp}, atk = {self.atk}, res = {self.res}, spd = {self.spd}")

    def __repr__(self) -> None:
        print(f"Character Object: name = {self.name}, lvl = {self.lvl}, exp = {self.exp}, atr = {self.atr}, hp = {self.hp}, atk = {self.atk}, res = {self.res}, spd = {self.spd}")

    def get_name(self) -> str:
        return self.name

    def get_hp(self) -> int:
        return self.hp

    def get_spd(self) -> int:
        return self.spd

    def choose_action(self):
        action = input(f"{self.name} choose an action:\n1 = Attack\n2 = Defend\n3 = Flee\n> ")
        print()
        if action == "1":
            print(f"{self.name} Attacked")
            return 1
        elif action == "2":
            print(f"{self.name} Defended")
            return 2
        elif action == "3":
            print(f"{self.name} Fled")
            return 3
        else:
            self.choose_action()
