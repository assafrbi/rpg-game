from classes.player import Colors, Person
from classes.enemy import Monster, Soldier
import random

round_number = 1


class Battle:
    def __init__(self, enemy, players):
        # self.Enemy = self.generate_enemy()
        self.enemy = enemy
        self.players = players

    def generate_enemy(self):
        enemy_op = [Monster, Soldier]
        enemy_1 = enemy_op[random.randint(0, 1)]("enemy_1")
        enemy_2 = enemy_op[random.randint(0, 1)]("enemy_2")
        enemy_op = [enemy_1, enemy_2]
        return enemy_op

    def start_fight(self):
        run = True
        while run:
            self.print_start()
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
        print(Colors.BOLD + "    End of round: "+str(round_number) + "\n" + Colors.END)
        self.print_players()
        self.print_enemy()
        print(Colors.BOLD +"\n"+ "=====================" + Colors.END)

    def print_start(self):
        global round_number
        print(Colors.BOLD + "=====================" + Colors.END)
        print(Colors.BOLD + "    Begin of round: " + str(round_number) + "\n" + Colors.END)
        round_number += 1

    def attack(self):
        for player_one in self.players:
            if self.is_finish() is True:
                break
            if player_one.is_dead() is False:
                run = True
                while run:
                    print("\n" + Colors.BOLD + player_one.get_name() + Colors.END)
                    player_one.choose_action()
                    choice = int(input("choose action: ")) - 1
                    if choice == 0:
                        self.normal_attack(player_one)
                        run = False
                    elif choice == 1:
                        player_one.choose_magic()
                        magic_num = int(input("choose magic: ")) - 1
                        if magic_num > len(player_one.magics) or magic_num < 0:
                            print(Colors.FAIL + "Please choose again" + Colors.END)
                            continue
                        if player_one.check_mp(magic_num) < 0:
                            print(Colors.FAIL + "You dont have enough MP, please choose again" + Colors.END)
                            continue
                        if player_one.get_spell_type(magic_num) == "black":
                            self.black_magic(player_one.magics[magic_num], player_one)
                            run = False
                        else:
                            self.white_magic(player_one.magics[magic_num], player_one)
                            run = False
                    elif choice == 2:
                        item = self.item_choose(player_one)
                        if item is False:
                            print(Colors.FAIL + "Please choose again" + Colors.END)
                            continue
                        if item.get_amount() <= 0:
                            print(Colors.FAIL + "You dont have any, please choose again" + Colors.END)
                            continue
                        else:
                            self.item_func(item, player_one)
                            run = False
                    else:
                        print(Colors.FAIL + "Not valid, Please choose again" + Colors.END)
                        continue

    def enemy_attack(self):
        enemy_dmg = self.enemy.generate_damage()
        live_hero = True
        while live_hero:
            hero = self.players[random.randint(0, len(self.players) - 1)]
            if hero.is_dead() is False:
                hero.set_hp((-1)*enemy_dmg)
                if hero.is_dead():
                    print(Colors.FAIL + "The enemy killed ", hero.get_name() + Colors.END)
                    live_hero = False
                else:
                    print(Colors.BOLD+Colors.FAIL+"The enemy attacked ",
                          hero.get_name(), "for" + str(enemy_dmg) +
                          " points of damage."+Colors.END+Colors.END)
                    live_hero = False

    def item_choose(self, player_one):
        player_one.choose_item()
        item_num = int(input("choose item: ")) - 1
        if item_num > len(player_one.items) or item_num < 0:
            return False
        else:
            return player_one.items[item_num]

    def item_func(self, item, player_one):
        item.set_amount()
        if item.get_type() == "heal":
            self.heal_item(item, player_one)
        elif item.get_type() == "mp":
            self.mp_item(item, player_one)
        elif item.get_type() == "damage":
            self.damage_item(item)
        else:
            self.strength_item(item, player_one)

    def heal_item(self, item, player_one):
        player_one.set_hp(item.get_prop())
        print("You used:", Colors.BOLD, item.get_name(), Colors.END, "HP restore by:", item.get_prop(), "points")

    def mp_item(self, item, player_one):
        player_one.set_hp(item.get_prop())
        print("You used:", Colors.BOLD, item.get_name(), Colors.END, "MP restore by:", item.get_prop(), "points")

    def damage_item(self, item):
        self.enemy.set_hp((-1)*item.get_prop())
        print("You attacked with:", Colors.BOLD, item.get_name(), Colors.END, "You caused:", item.get_prop(), "damage")

    def strength_item(self, item, player_one):
        player_one.set_atk(item.get_prop())
        print("You used:", Colors.BOLD, item.get_name(), Colors.END, "attack upgrade by:", item.get_prop(), "points")

    def normal_attack(self, player_one):
        dmg = player_one.generate_damage()
        if self.enemy.get_df()-dmg < 0:
            self.enemy.set_hp(self.enemy.get_df()-dmg)
            print(Colors.BOLD + "You attacked for", dmg, "points of damage." + Colors.END)

    def is_finish(self):
        if self.enemy.get_hp() == 0:
            return True

        for player in self.players:
            if not player.is_dead():
                return False
        return True

    def get_magic_type(self, i, player_one):
        return player_one.magics[i].get_type

    def white_magic(self, my_magic, player_one):
        healing = my_magic.generate_spell_damage()
        player_one.set_mp((-1) * my_magic.get_cost())
        player_one.set_hp(healing)
        print("The magic", my_magic.get_name(), "heals you ", healing, "points.")

    def black_magic(self, my_magic, player_one):
        player_one.set_mp((-1) * my_magic.get_cost())
        dmg = my_magic.generate_spell_damage()
        self.enemy.set_hp((-1)*dmg)
        print("The magic", my_magic.get_name(), "deals ", dmg, "points of damage.")

    def print_enemy(self):
        self.enemy.print_status()

    def print_players(self):
        for player in self.players:
            player.print_status()
