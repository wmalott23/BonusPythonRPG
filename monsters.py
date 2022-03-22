from moves import Moves
from random import Random, randint

class Monster:
    def __init__(self, name, health, moveset):
        self.name = name
        self.att_dam = 0
        self.health = health
        self.moveset = moveset

    def attack(self):
        num = randint(0,2)
        damage = self.moveset[num].attack_power
        self.att_dam = damage
        print(f'{self.name} attacks with {self.moveset[num].name} for {self.moveset[num].attack_power} damage')