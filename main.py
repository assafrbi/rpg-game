from game.battle import *
from classes.inventory import *

# create players

assaf = Person("assaf", 3400, 35, 30, 10,1)
liat = Person("liat", 1400, 55, 30, 10,1)

enemy = Person("covid19", 5100, 25, 30, 1500,1)

players = [assaf, liat]

running = True

print("****let the battle begin****")
while running:
    for player_one in players:
        cycle = Battle(enemy,players)
        running = cycle.start_fight()

print("************")
print("End of Game")
print("************")
