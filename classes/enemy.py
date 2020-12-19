
from classes.player import Person

monster_number = 1
soldier_number = 1
leader_number = 1


class Monster:
    def __init__(self):
        global monster_number
        self.player = Person("Monster_" + str(monster_number), 300, 20, 20, 5, 15, 1)
        monster_number += 1

    def get_player(self):
        return self.player

    def get_name(self):
        return self.get_player().get_name()


class Soldier:
    def __init__(self):
        global soldier_number
        self.player = Person("Soldier_" + str(soldier_number), 200, 25, 25, 5, 15, 1)
        soldier_number += 1

    def get_player(self):
        return self.player

    def get_name(self):
        return self.get_player().get_name()


class Leader:
    def __init__(self):
        global leader_number
        self.player = Person("Monster_" + str(leader_number), 300, 35, 25, 7, 20, 1)
        leader_number += 1

    def get_player(self):
        return self.player

    def get_name(self):
        return self.get_player().get_name()
