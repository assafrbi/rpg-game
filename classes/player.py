import math
import random
from classes.spell import Magic
from classes.inventory import Item

# create the spells
fire = Magic("Fire", 10, 20, "black")
quake = Magic("quake", 20, 50, "black")
electricity = Magic("electricity", 5, 9, "black")
blizzard = Magic("blizzard", 2, 3, "black")
heal = Magic("heal", 5, 40, "white")

magic = [fire, quake, electricity, blizzard, heal]

# create inventory
potion = Item("Potion", "heal", "heals 10 HP", 10)
hi_potion = Item("hi_potion", "heal", "heals 20 HP", 20)
super_potion = Item("super_potion", "heal", "heals 50 HP", 50)
mp_potion = Item("mp_potion", "mp", "Extra 20 MP", 20)
power = Item("power", "strength", "Extra 10 Attack points", 10)
sword = Item("Sword", "damage", "Deals 30 HP", 30)
bow = Item("bow", "damage", "Deals 20 HP", 20)

inventory = [potion, hi_potion, super_potion, mp_potion, power, sword, bow]


class Colors:
    FAIL = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    WARNING = '\033[93m'
    HEADER = '\033[95m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df,live):
        self.live = live
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.atk = atk
        self.name = name
        self.df = df
        self.magics = magic
        self.actions = ["Attack", "Magic", "Use item from inventory"]
        self.items = inventory

    def generate_damage(self):
        atk_low = self.atk - 10
        atk_high = self.atk + 10
        return random.randrange(atk_low, atk_high)

    def get_hp(self):
        return self.hp

    def get_df(self):
        return self.df

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
        if self.hp <= 0:
            self.hp = 0

    def set_atk(self, i):
        self.atk += i

    def set_mp(self, i):
        self.mp += i
        if self.mp > self.max_mp:
            self.mp = self.max_mp

    def get_max_hp(self):
        return self.max_hp

    def get_max_mp(self):
        return self.max_mp

    def get_mp(self):
        return self.mp

    def get_magics(self):
        return self.magics

    def check_mp(self, i):
        return self.mp - self.magics[i].get_cost()

    def get_spell_name(self, i):
        return self.magics[i].get_name()

    def get_spell_type(self, i):
        return self.magics[i].get_type()

    def get_item(self, i):
        return self.items[i].get_amount()

    def choose_action(self):
        i = 1
        print(Colors.BLUE + "\n" + "action options: " + Colors.END)
        for action in self.actions:
            print(str(i) + ":", action)
            i += 1

    def choose_magic(self):
        i = 0
        print(Colors.BLUE + "\n" + "magic options: " + Colors.END)
        for item in self.magics:
            print(str(i + 1) + ":", item.get_name(), "(cost:", str(item.get_cost()) + ")")
            i += 1

    def choose_item(self):
        i = 0
        print(Colors.BLUE + "\n" + "inventory options: " + Colors.END)
        for item in self.items:
            print(str(i + 1) + ":", item.get_name(), "(Amount:", str(item.get_amount()) + ")")
            i += 1

    def print_status(self):
        spaceHP = 15
        spaceMP = 30
        space = 2
        blocks_h = math.ceil(((self.get_hp() / self.get_max_hp())/4)*100)
        block_m = math.ceil((self.get_mp() / self.get_max_mp())*10)
        print("NAME{0}HP{1}MP".format(" " * spaceHP, " " * spaceMP))
        print("{bold}{space_hp}{end}{get_hp}{blockg}{mp}{space_mp}{get_mp}{blockb}".format(
            bold=Colors.BOLD + self.get_name(),
            end=Colors.END,
            space_hp=" " * (spaceHP - len(self.get_name())),
            get_hp=" "*(3-len(str(self.get_hp())))+str(self.get_hp()) + "/" + str(self.get_max_hp()),
            blockg="|" + Colors.GREEN + "█" * blocks_h + Colors.END,
            mp=" " * (25 - blocks_h) + "|",
            get_mp=" "*(2-len(str(self.get_mp())))+str(self.get_mp()) + "/" + str(self.get_max_mp()),
            blockb="|" + Colors.BLUE + "█" * block_m + Colors.END + " " * (10 - block_m) + "|",
            space_mp=" " * 5
        ))
