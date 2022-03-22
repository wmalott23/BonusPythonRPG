# As a developer, I want to make at least five commits on GitHub with descriptive 
# messages.  
 
# As a user, I want an engaging story to be told using print() statements.  
 
# As a user, I want Hercules (and each enemy), to have health, attack power, and a 
# List of attack names saved in a Dictionary. 
 
# As a user, I want the ability to select Hercules’ attack using a menu prompt. 
 
# As a user, I want the foe’s attack to be chosen at random. 
 
# As a user, I want the results of each attack to be logged in the terminal.  
 
# As a developer, I want to use an Attack() function that will terminate when 
# Hercules or an enemy’s health reaches zero.  
 
# As a developer, I want my RunGame() function to call my other functions in a 
# logical order that will determine game flow. 
 
# As a developer, I want all of my functions to have a Single 
# Responsibility. Remember, each function should do just one thing!  
 
from character import Character
import random

hercules = Character("Hercules", 100, 42)
hercules.add_move("Smol Punch", 1, 0, 0)
hercules.add_move("Big Punch", 2, 0, 3)
hercules.add_move("Heal Punch", 0, 1, 0)
hercules.add_move("Metronome", random.randint(0, 3), random.randint(0,3), 5)

goblin = Character("Goblin", 50, 7)
goblin.add_move("Smol_punch", hercules.attack, 0, 1, "You do a smol punch")
hercules.add_move("Heal_punch", 0, hercules.attack, 1, "You do a heal punch")