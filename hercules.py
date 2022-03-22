from moves import Moves

class Hercules:
    def __init__(self):
        self.health = 100
        self.moveset = [Moves("Smol Punch", 20)]
        self.pot_move = [Moves("Big Punch", 40),Moves("Heal Punch", 20), Moves("Guard Punch", 00), Moves("Hyper Beam"), 100]

    def attack(self):
        confirm = 0
        while confirm != 1:
            for each in self.moveset:
                print(each.name)
            user_choice = input("What move would you like to use?")
            for each in self.moveset:
                if each.name == user_choice:
                    print(f"Hercules attacks with a {each.name}, doing {each.attack_power} damage!")
                    confirm = 1

    def add_move(self):
        pass