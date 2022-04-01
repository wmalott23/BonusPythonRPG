from monsters import Monster
from moves import Moves
from random import randint

class Bushel:
    def __init__(self, gen_num):
        self.mons = [0]
        self.gen_mon(gen_num)

    def gen_mon(self, set_num):
        if set_num == 1:
            mon_moves = [Moves("Cut", 10), Moves("Slap", 10), Moves("Screech", 10)]
            num = randint(0,2)
            mons = [Monster("Goblin", 30, mon_moves), Monster("Smol Goblin", 20, mon_moves), Monster("Big Goblin", 40, mon_moves)]
            mon_choice = mons[num]
            self.mons[0] = mon_choice
        if set_num == 2:
            mon_moves = [Moves("Roar", 20), Moves("Charge", 10), Moves("Maul", 15)]
            num = randint(0,2)
            mons = [Monster("Lion", 30, mon_moves), Monster("Tiger", 25, mon_moves), Monster("Bear", 40, mon_moves)]
            mon_choice = mons[num]
            self.mons[0] = mon_choice
        if set_num == 3:
            mon_moves = [Moves("Poke", 10), Moves("Prod", 15), Moves("Stab", 30)]
            num = randint(0,2)
            mons = [Monster("Demon", 30, mon_moves), Monster("Small Demon", 25, mon_moves), Monster("Big Demon", 50, mon_moves)]
            mon_choice = mons[num]
            self.mons[0] = mon_choice
        if set_num == 4:
            self.mons[0] = Monster("Nemean Lion", 100, [Moves("Roar", 25), Moves("Swipe", 30), Moves("Smol Punch", 20)])
        if set_num == 5:
            self.mons[0] = Monster("Lernaean Hydra", 100, [Moves("Roar", 25), Moves("Swipe", 30), Moves("Smol Punch", 20)])
        if set_num == 6:
            self.mons[0] = Monster("Cerberus", 100, [Moves("Roar", 25), Moves("Swipe", 30), Moves("Smol Punch", 20)])
