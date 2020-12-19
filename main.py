from game.battle import Battle

if __name__ == "__main__":
    running = True
    while running:
        cycle = Battle()
        running = cycle.start_fight()

    print("************")
    print("End of Game")
    print("************")
