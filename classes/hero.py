from classes.player import Person

human_number = 1
angel_number = 1
magician_number = 1

class Human:
    def __init__(self):
        global human_number
        self.player = Person("human_" + str(human_number), 200, 20, 25, 9, 15, 1)
        human_number += 1

    def get_player(self):
        return self.player

    def get_name(self):
        return self.get_player().get_name()

    def get_advantage(self):
        return "High attack ,High defense"


class Angel:
    def __init__(self):
        global angel_number
        self.player = Person("angel_" + str(angel_number), 250, 35, 15, 6, 30, 1)
        angel_number += 1

    def get_player(self):
        return self.player

    def get_name(self):
        return self.get_player().get_name()

    def get_advantage(self):
        return "High hp,High m_defense"


class Magician:
    def __init__(self):
        global magician_number
        self.player = Person("magician_" + str(magician_number), 150, 35, 15, 3, 30, 1)
        magician_number += 1

    def get_player(self):
        return self.player

    def get_name(self):
        return self.get_player().get_name()

    def get_advantage(self):
        return "High magic,High m_defense"