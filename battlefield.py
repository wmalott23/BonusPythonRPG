from hercules import Hercules
from bushel import Bushel
from random import randint

class Battlefield:
    def __init__(self, bush_num):
        herc = Hercules
        bushel = Bushel(bush_num)

    def run_match(self):
        self.display_welcome()
        self.battle()
        self.display_winners()
        self.choose_reward()

    def display_welcome(self):
        print(f'A wild {self.bushel.mons[0].name} appears.')

    def battle(self):
        self.herc.health = 100
        herc_health = self.herc.health
        mon_health = self.bushel.mons[0].health
        counter = 1
        while herc_health > 0 and mon_health > 0:
            if counter == 1:
                self.herc_turn()
                counter = 2
            if counter == 2:
                self.mon_turn()
                counter = 1
            herc_health = self.herc.health
            mon_health = self.bushel.mons[0].health

    def herc_turn(self):
        self.herc.attack()
        self.mon_health -= self.herc.att_dam
    
    def mon_turn(self):
        self.mon.attack()
        self.herc.health -= self.bushel.mon.att_dam

    def display_winners(self):
        herc_health = self.herc.health
        mon_health = self.bushel.mons[0].health
        if herc_health <= 0:
            print("Hercules has died :(")
        if mon_health <= 0:
            print("Hercules is victorious!")


    def choose_reward(self):
        rew = randint(0,4)
        if rew == 4:
            self.herc.add_move()