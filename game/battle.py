from classes.player import Colors
from classes.enemy import Monster, Soldier, Leader
from classes.hero import Angel, Human, Magician
import random

round_number = 1


def black_magic(my_magic, player_one, enemy):
    dmg = enemy.get_dfm() - my_magic.generate_spell_damage()
    player_one.set_mp((-1) * my_magic.get_cost())
    if dmg < 0:
        enemy.set_hp(dmg)
    print("The magic", my_magic.get_name(), "deals ", str((-1) * dmg), "points of damage.")


def white_magic(my_magic, player_one):
    healing = my_magic.generate_spell_damage()
    player_one.set_mp((-1) * my_magic.get_cost())
    player_one.set_hp(healing)
    print("The magic", my_magic.get_name(), "heals you ", healing, "points.")


def get_magic_type(i, player_one):
    return player_one.magics[i].get_type


def normal_attack(player_one, enemy):
    dmg = enemy.get_df() - player_one.generate_damage()
    if dmg < 0:
        enemy.set_hp(dmg)
        print(Colors.BOLD + "You attacked for", str((-1) * dmg), "points of damage." + Colors.END)
    else:
        print(Colors.BOLD + "You are to wick to make any damage" + Colors.END)


def strength_item(item, player_one):
    player_one.set_atk(item.get_prop())
    print("You used:", Colors.BOLD, item.get_name(), Colors.END, "attack upgrade by:", item.get_prop(), "points")


def damage_item(item, enemy):
    enemy.set_hp((-1) * item.get_prop())
    print("You attacked with:", Colors.BOLD, item.get_name(), Colors.END, "You caused:", item.get_prop(), "damage")


def mp_item(item, player_one):
    player_one.set_hp(item.get_prop())
    print("You used:", Colors.BOLD, item.get_name(), Colors.END, "MP restore by:", item.get_prop(), "points")


def heal_item(item, player_one):
    player_one.set_hp(item.get_prop())
    print("You used:", Colors.BOLD, item.get_name(), Colors.END, "HP restore by:", item.get_prop(), "points")


def item_choose(player_one):
    player_one.choose_item()
    item_num = int(input("choose item: ")) - 1
    if item_num > len(player_one.items) or item_num < 0:
        return False
    else:
        return player_one.items[item_num]


def item_func(item, player_one, enemy):
    item.set_amount()
    if item.get_type() == "heal":
        heal_item(item, player_one)
    elif item.get_type() == "mp":
        mp_item(item, player_one)
    elif item.get_type() == "damage":
        damage_item(item, enemy)
    else:
        strength_item(item, player_one)


def print_start():
    global round_number
    print(Colors.BOLD + "=====================" + Colors.END)
    print(Colors.BOLD + "    Begin of round: " + str(round_number) + "\n" + Colors.END)


def hero_list():
    hero = 0
    while hero == 0:
        print(Colors.BLUE + "\n" + "Hero's options: " + Colors.END)
        print("{i}{name}{adv}".format(i="1. ", name="Human   ", adv="(The advantage: High attack ,High defense)"))
        print("{i}{name}{adv}".format(i="2. ", name="Angel   ", adv="(The advantage: High hp,High m_defense)   "))
        print("{i}{name}{adv}".format(i="3. ", name="Magician", adv="(The advantage: High magic,High m_defense)"))
        choose = int(input())
        if choose == 1:
            hero = Human()
        elif choose == 2:
            hero = Angel()
        elif choose == 3:
            hero = Magician()
        else:
            print(Colors.BOLD + "not valid..please choose again" + Colors.END)
    return hero


def generate_players():
    players = ["", ""]
    print("{0}{1}{2}".format(Colors.BOLD + Colors.BLUE, "***WELCOME TO THE GAME***", Colors.END + Colors.END))
    print("{0}{1}{2}".format(Colors.BOLD + Colors.BLUE, "Please choose 2 Hero's", Colors.END + Colors.END))
    print("{0}{1}{2}".format(Colors.BOLD, "First choose: ", Colors.END))
    players[0] = hero_list()
    print("{0}{1}{2}".format(Colors.BOLD, "Second choose: ", Colors.END))
    players[1] = hero_list()
    return players


def generate_enemy():
    enemy = ["", ""]
    num = 0
    while num < 2:
        rnd = random.randint(0, 2)
        if rnd == 1:
            enemy[num] = Leader()
        elif rnd == 2:
            enemy[num] = Soldier()
        else:
            enemy[num] = Monster()
        num += 1
    return enemy


class Battle:
    def __init__(self):
        self.enemy = generate_enemy()
        self.players = generate_players()

    def start_fight(self):
        run = True
        while run:
            print_start()
            coin = random.randint(0, 1)
            if coin == 1:
                self.enemy_attack()
                if self.is_finish() is True:
                    print(Colors.FAIL + "You lost!!" + Colors.END)
                    break
                self.attack()
                if self.is_finish() is True:
                    print(Colors.GREEN + "Winner!!" + Colors.END)
                    break
                self.print_all()
            else:
                self.attack()
                if self.is_finish() is True:
                    print(Colors.GREEN + "Winner!!" + Colors.END)
                    break
                self.enemy_attack()
                if self.is_finish() is True:
                    print(Colors.FAIL + "You lost!!" + Colors.END)
                    break
                self.print_all()
        return False

    def print_all(self):
        global round_number
        print(Colors.BOLD + "=====================" + Colors.END)
        print(Colors.BOLD + "    End of round: " + str(round_number) + "\n" + Colors.END)
        self.print_players()
        self.print_enemy()
        print(Colors.BOLD + "\n" + "=====================" + Colors.END)
        round_number += 1

    def attack(self):
        for player_one in self.players:
            if self.is_finish() is True:
                break
            if player_one.get_player().is_dead() is False:
                run = True
                enemy = 0
                while enemy == 0:
                    num = random.randint(0, 1)
                    if not self.enemy[num].get_player().is_dead():
                        enemy = self.enemy[num].get_player()
                while run:
                    print("\n" + Colors.BOLD + player_one.get_name() + Colors.END)
                    player_one.get_player().choose_action()
                    choice = int(input("choose action: ")) - 1
                    if choice == 0:
                        normal_attack(player_one.get_player(), enemy)
                        run = False
                    elif choice == 1:
                        player_one.get_player().choose_magic()
                        magic_num = int(input("choose magic: ")) - 1
                        if magic_num > len(player_one.get_player().magics) or magic_num < 0:
                            print(Colors.FAIL + "Please choose again" + Colors.END)
                            continue
                        if player_one.get_player().check_mp(magic_num) < 0:
                            print(Colors.FAIL + "You dont have enough MP, please choose again" + Colors.END)
                            continue
                        if player_one.get_player().get_spell_type(magic_num) == "black":
                            black_magic(player_one.get_player().magics[magic_num], player_one.get_player(), enemy)
                            run = False
                        else:
                            white_magic(player_one.get_player().magics[magic_num], player_one.get_player())
                            run = False
                    elif choice == 2:
                        item = item_choose(player_one.get_player())
                        if item is False:
                            print(Colors.FAIL + "Please choose again" + Colors.END)
                            continue
                        if item.get_amount() <= 0:
                            print(Colors.FAIL + "You dont have any, please choose again" + Colors.END)
                            continue
                        else:
                            item_func(item, player_one, enemy)
                            run = False
                    else:
                        print(Colors.FAIL + "Not valid, Please choose again" + Colors.END)
                        continue

    def enemy_attack(self):
        for enemy in self.enemy:
            live_hero = True
            while live_hero:
                hero = self.players[random.randint(0, len(self.players) - 1)]
                if hero.get_player().is_dead() is False:
                    enemy_dmg = hero.get_player().get_df() - enemy.get_player().generate_damage()
                    if enemy_dmg < 0:
                        hero.get_player().set_hp(enemy_dmg)
                        if hero.get_player().is_dead():
                            print(Colors.FAIL + "The enemy killed ", hero.get_name() + Colors.END)

                        else:
                            print(Colors.BOLD + Colors.FAIL + "The enemy attacked ", hero.get_name(),
                                  "for " + str((-1) * enemy_dmg) +
                                  " points of damage." + Colors.END + Colors.END)
                    else:
                        print(Colors.BOLD + "The enemy is weak and can't heart you ", hero.get_name() + Colors.END)
                    live_hero = False

    def is_finish(self):
        sum_enemy = 2
        for enemy in self.enemy:
            if enemy.get_player().is_dead():
                sum_enemy -= 1
        if sum_enemy == 0:
            return True

        for player in self.players:
            if not player.get_player().is_dead():
                return False
        return True

    def print_enemy(self):
        for enemy in self.enemy:
            enemy.get_player().print_enemy_status()

    def print_players(self):
        for player in self.players:
            player.get_player().print_status()
