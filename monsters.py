from moves import Moves

class Monster:
    def __init__(self, name, health, move_num):
        self.name = name
        self.health = health
        self.moveset = []

    def attack(self):
        pass