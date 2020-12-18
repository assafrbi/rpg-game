import random


def generate_damage(self):
    atk_low = self.atk - 10
    atk_high = self.atk + 10
    return random.randrange(atk_low, atk_high)


def take_damage(self, dmg):
    self.hp -= dmg
    if self.hp <= 0:
        self.hp = 0


def get_hp(self):
    return self.hp


def is_dead(self):
    if self.get_hp() == 0:
        self.live = 0
        return True
    else:
        return False


def get_name(self):
    return self.name


def set_hp(self, i):
    self.hp += i
    if self.hp > self.max_hp:
        self.hp = self.max_hp


def set_atk(self, i):
    self.atk += i


class Monster:
    def __init__(self, name):
        self.live = 1
        self.hp = 100
        self.max_hp = 100
        self.atk = 25
        self.name = name
        self.df = 0
        self.actions = ["Attack", "sleep"]

    def action(self):
        if get_hp(self) < 25:
            return "Sleep"
        else:
            return "Attack"


class Soldier:
    def __init__(self, name):
        self.live = 1
        self.hp = 100
        self.max_hp = 100
        self.atk = 10
        self.name = name
        self.df = 15
        self.actions = ["Attack", "Guard"]


class Leader:
    def __init__(self, name):
        self.live = 1
        self.hp = 100
        self.max_hp = 100
        self.atk = 10
        self.name = name
