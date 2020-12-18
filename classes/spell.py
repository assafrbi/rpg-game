import random


class Magic:
    def __init__(self, name, cost, dmg, magic_type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = magic_type

    def get_cost(self):
        return self.cost

    def get_dmg(self):
        return self.dmg

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def generate_spell_damage(self):
        dmg = self.get_dmg()
        dmg_low = dmg - 5
        dmg_high = dmg + 5
        return random.randrange(dmg_low, dmg_high)
