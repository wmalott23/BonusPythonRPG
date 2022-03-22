from moves import Moves

class Hercules:
    def __init__(self):
        self.health = 99
        self.att_dam = 0
        self.moveset = [Moves("Smol Punch", 20)]
        self.pot_move = [Moves("Big Punch", 40), Moves("Falcon Punch", 60), Moves("Hyper Beam", 100)]

    def attack(self):
        confirm = 0
        while confirm != 1:
            for each in self.moveset:
                print(each.name)
            user_choice = input("What move would you like to use?")
            for each in self.moveset:
                if each.name == user_choice:
                    self.att_dam = each.attack_power
                    print(f"Hercules attacks with a {each.name}, doing {each.attack_power} damage!")
                    confirm = 1

    def add_move(self):
        confirm = 0
        while confirm != 1:
            for each in self.pot_move:
                print(each.name)
            add_choice = input("Which move would you like to learn?")
            for each in self.pot_move:
                if each.name == add_choice:
                    self.moveset.append(each)
                    self.pot_move.remove(each)
                    confirm = 1