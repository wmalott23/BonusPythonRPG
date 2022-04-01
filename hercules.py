from moves import Moves

move = [Moves("Smol Punch", 20)]
pot_moveset = [Moves("Big Punch", 40), Moves("Falcon Punch", 60), Moves("Hyper Beam", 100)]
health = 99

class Hercules:
    def __init__(self):
        self.health = health
        self.att_dam = 0
        self.moveset = move
        self.pot_move = pot_moveset


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
        while confirm != 1 and self.pot_move != []:
            for each in pot_moveset:
                print(each.name)
            add_choice = input("Which move would you like to learn?")
            for each in pot_moveset:
                if each.name == add_choice:
                    move.append(each)
                    pot_moveset.remove(each)
                    confirm = 1