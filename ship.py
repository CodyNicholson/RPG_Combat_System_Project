import random

class Ship:
    def __init__(self, name:str, typ:str, lvl:int, exp:int, hp:int, atk : int, res : int, spd: int):
        self.name = name
        self.typ = typ
        self.lvl = 1 if (lvl == None) else lvl
        self.exp = 0 if (exp == None) else exp
        self.temp_exp = 0
        self.base_hp = hp
        self.temp_hp = hp
        self.base_atk = atk
        self.temp_atk = atk
        self.base_res = res
        self.temp_res = res
        self.base_spd = spd
        self.temp_spd = spd
        #print(f"Ship: name = {self.get_name()}, lvl = {self.get_lvl()}, exp = {self.get_exp()}, typ = {self.get_typ()}, hp = {self.get_base_hp()}, atk = {self.get_base_atk()}, res = {self.get_base_res()}, spd = {self.get_base_spd()}")

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

    def get_temp_exp(self) -> int:
        return self.temp_exp

    def set_temp_exp(self, exp) -> None:
        self.temp_exp = exp

    def increase_temp_exp(self, exp) -> None:
        self.temp_exp += exp

    def get_base_hp(self) -> int:
        return self.base_hp

    def set_base_hp(self, hp) -> None:
        self.base_hp = hp

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
        action = ""
        actions = ["1", "2", "3"]
        while action not in actions:
            action = input(f"The {self.name} is awaiting orders:\n1 = Fire Cannon\n2 = Drop Bombs\n3 = Launch Torpedoes\n4 = Concede\n> ")
            print()
            if action == "1":
                return 1
            elif action == "2":
                return 2
            elif action == "3":
                return 3
            elif action == "4":
                print(f"{self.name} conceded\n")
                return 4

    def take_damage(self, dmg) -> bool:
        temp_hp = self.get_temp_hp()
        temp_res = self.get_temp_res()
        dmg_after_res = (dmg - temp_res) if ((dmg - temp_res) > 0) else 0
        new_hp_val = (temp_hp - dmg_after_res)
        self.set_temp_hp(new_hp_val)

        if (new_hp_val > 0) and (dmg_after_res > 0):
            print(f"The {self.get_name()} had {temp_hp} hp then took {dmg_after_res} damage and now has {new_hp_val} hp left\n")
            return False
        elif (new_hp_val > 0) and (dmg_after_res <= 0):
            print(f"The {self.get_name()} resisted all damage and still has {new_hp_val} hp left\n")
            return False
        else:
            print(f"The {self.get_name()} had {temp_hp} hp then took {dmg_after_res} damage and was destroyed\n")
            return True

    def sunk(self) -> bool:
        return self.get_temp_hp() <= 0

    def defend(self) -> None:
        temp_res = self.get_temp_res()
        self.set_temp_res(temp_res * 2)

    def concede(self) -> None:
        print(f"The {self.get_name()} conceded from the battle\n")
        self.set_temp_hp(0)

    def total_exp(self) -> None:
        current_lvl = self.get_lvl()
        current_exp = self.get_exp() + self.get_temp_exp()
        while (current_exp >= 100):
            current_lvl += 1
            self.level_up(current_lvl)
            current_exp -= 100
        if current_exp < 100:
            print(f"\nThe {self.get_name()} gained {self.get_temp_exp()} exp this battle and now has {current_exp} exp")
            self.set_exp(current_exp)
        else:
            print(f"\nIn addition to leving up, The {self.get_name()} gained {current_exp} exp this battle")
    
    def level_up(self, current_lvl:int) -> None:
        self.set_lvl(current_lvl)
        current_hp = self.get_base_hp()
        current_atk = self.get_base_atk()
        current_res = self.get_base_res()
        current_spd = self.get_base_spd()
        hp_increase = round((((random.randint(0,10) / 100) + 1) * current_hp))
        atk_increase = round((((random.randint(0,10) / 100) + 1) * current_atk))
        res_increase = round((((random.randint(0,10) / 100) + 1) * current_res))
        spd_increase = round((((random.randint(0,10) / 100) + 1) * current_spd))
        self.set_base_hp(hp_increase)
        self.set_base_atk(atk_increase)
        self.set_base_res(res_increase)
        self.set_base_spd(spd_increase)
        print(f"\n<********** LEVEL UP **********>\nThe {self.get_name()} grew to level {current_lvl}!\nHP: {current_hp} -> {hp_increase}\nATK: {current_atk} -> {atk_increase}\nRES: {current_res} -> {res_increase}\nSPD: {current_spd} -> {spd_increase}\n<******************************>")
