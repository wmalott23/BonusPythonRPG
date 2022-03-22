from hercules import Hercules
from bushel import Bushel
from random import randint

class Battlefield:
    def __init__(self, bush_num):
        self.herc = Hercules()
        self.bushel = Bushel(bush_num)

    def run_match(self):
        self.display_welcome()
        self.battle()
        self.display_winners()
        self.choose_reward()

    def display_welcome(self):
        print(f'A wild {self.bushel.mons[0].name} appears.')
        print("I choose you! Hercules!")

    def battle(self):
        herc_health = self.herc.health
        mon_health = self.bushel.mons[0].health
        counter = 2
        while herc_health > 0 and mon_health > 0:
            if counter == 2:
                self.mon_turn()
                counter = 1
                herc_health = self.herc.health
                print(f'Hercules has {self.herc.health} HP left')
            if counter == 1 and herc_health > 0:
                self.herc_turn()
                counter = 2
                mon_health = self.bushel.mons[0].health
                print(f'Goblin has {mon_health} HP left')

    def herc_turn(self):
        self.herc.attack()
        self.bushel.mons[0].health -= self.herc.att_dam
    
    def mon_turn(self):
        self.bushel.mons[0].attack()
        self.herc.health -= self.bushel.mons[0].att_dam

    def display_winners(self):
        herc_health = self.herc.health
        mon_health = self.bushel.mons[0].health
        if herc_health <= 0:
            print("Hercules has died :(. Please try again!")
            self.run_match()
        if mon_health <= 0:
            print("Hercules is victorious!")


    def choose_reward(self):
        rew = randint(0,4)
        if rew == 4:
            self.herc.add_move()