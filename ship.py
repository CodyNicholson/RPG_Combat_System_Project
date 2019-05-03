
class Ship:
    def __init__(self, name:str, typ:str, lvl:int, exp:int, hp:int, atk : int, res : int, spd: int):
        self.name = name
        self.typ = typ
        self.lvl = 1 if (lvl == None) else lvl
        self.exp = 0 if (exp == None) else exp
        self.hp = hp
        self.r_hp = hp
        self.atk = atk
        self.res = res
        self.spd = spd
        print(f"New ship: name = {self.name}, lvl = {self.lvl}, exp = {self.exp}, typ = {self.typ}, hp = {self.hp}, r_hp = {self.r_hp}, atk = {self.atk}, res = {self.res}, spd = {self.spd}")

    def get_name(self) -> str:
        return self.name

    def get_typ(self) -> str:
        return self.typ

    def get_lvl(self) -> int:
        return self.lvl

    def get_exp(self) -> int:
        return self.exp

    def get_hp(self) -> int:
        return self.hp

    def get_r_hp(self) -> int:
        return self.r_hp

    def get_atk(self) -> int:
        return self.atk

    def get_res(self) -> int:
        return self.res

    def get_spd(self) -> int:
        return self.spd

    def choose_action(self) -> int:
        action = input(f"The {self.name} is awaiting orders:\n1 = Attack\n2 = Defend\n3 = Concede\n> ")
        print()
        if action == "1":
            return 1
        elif action == "2":
            print(f"{self.name} took evasive actions\n")
            return 2
        elif action == "3":
            print(f"{self.name} conceded\n")
            return 3
        else:
            self.choose_action()

    def take_damage(self, dmg) -> bool:
        dmg -= self.res
        self.r_hp = self.r_hp - dmg
        if self.get_r_hp() > 0:
            print(f"The {self.name} had {self.r_hp + dmg} hp then took {dmg + self.res} but resisted {self.res} damage and now has {self.r_hp} hp left\n")
            return False
        else:
            print(f"The {self.name} had {self.r_hp + dmg} hp then took {dmg} damage and was destroyed\n")
            return True
