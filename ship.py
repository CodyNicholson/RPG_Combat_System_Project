class Ship:
    def __init__(self, name:str, typ:str, lvl:int, exp:int, hp:int, atk : int, res : int, spd: int):
        self.name = name
        self.typ = typ
        self.lvl = 1 if (lvl == None) else lvl
        self.exp = 0 if (exp == None) else exp
        self.base_hp = hp
        self.temp_hp = hp
        self.base_atk = atk
        self.temp_atk = atk
        self.base_res = res
        self.temp_res = res
        self.base_spd = spd
        self.temp_spd = spd
        print(f"New ship: name = {self.name}, lvl = {self.lvl}, exp = {self.exp}, typ = {self.typ}, hp = {self.base_hp}, atk = {self.base_atk}, res = {self.base_res}, spd = {self.base_spd}")

    def get_name(self) -> str:
        return self.name

    def get_typ(self) -> str:
        return self.typ

    def get_lvl(self) -> int:
        return self.lvl

    def set_lvl(self, lvl) -> None:
        self.lvl = lvl

    def get_exp(self) -> int:
        return self.exp

    def set_exp(self, exp) -> None:
        self.exp = exp

    def get_base_hp(self) -> int:
        return self.base_hp

    def set_base_hp(self, hp) -> None:
        self.max_hp = hp

    def get_temp_hp(self) -> int:
        return self.temp_hp

    def set_temp_hp(self, hp) -> None:
        self.temp_hp = hp

    def get_base_atk(self) -> int:
        return self.base_atk

    def set_base_atk(self, atk) -> None:
        self.base_atk = atk

    def get_temp_atk(self) -> int:
        return self.temp_atk

    def set_temp_atk(self, atk) -> None:
        self.temp_atk = atk

    def get_base_res(self) -> int:
        return self.base_res

    def set_base_res(self, res) -> None:
        self.base_res = res

    def get_temp_res(self) -> int:
        return self.temp_res

    def set_temp_res(self, res) -> None:
        self.temp_res = res

    def get_base_spd(self) -> int:
        return self.base_spd

    def set_base_spd(self, spd) -> None:
        self.base_spd = spd

    def get_temp_spd(self) -> int:
        return self.temp_spd

    def set_temp_spd(self, spd) -> None:
        self.temp_spd = spd

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

    def take_damage(self, dmg) -> None:
        temp_hp = self.get_temp_hp()
        temp_res = self.get_temp_res()
        dmg_after_res = (dmg - temp_res) if ((dmg - temp_res) > 0) else 0
        new_hp_val = (temp_hp - dmg_after_res)
        self.set_temp_hp(new_hp_val)

        if (new_hp_val > 0) and (dmg_after_res > 0):
            print(f"The {self.get_name()} had {temp_hp} hp then took {dmg_after_res} damage and now has {new_hp_val} hp left\n")
        elif (new_hp_val > 0) and (dmg_after_res <= 0):
            print(f"The {self.get_name()} resisted all damage and still has {new_hp_val} hp left\n")
        else:
            print(f"The {self.get_name()} had {temp_hp} hp then took {dmg_after_res} damage and was destroyed\n")

    def sunk(self) -> bool:
        return self.get_temp_hp() <= 0

    def defend(self) -> None:
        temp_res = self.get_temp_res()
        self.set_temp_res(temp_res * 2)

    def concede(self) -> None:
        print(f"The {self.get_name()} conceded from the battle\n")
        self.set_temp_hp(0)
