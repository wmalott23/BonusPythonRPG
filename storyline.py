from battlefield import Battlefield
from hercules import Hercules
from random import randint

class Storyline:
    def __init__(self):
        self.herc = Hercules()

    def choose_reward(self):
        rew = randint(0,1)
        if rew == 1:
            self.herc.add_move()

    def run_game(self):
        self.intro()
        self.nem_lion()
        self.lern_hydra()
        self.cerb()
        self.end()

                    
    def intro(self):
        print("Zeus was a young boy from Pallet Town. Tomorrow, Zeus will turn 10 years old and finally be able to get his Pokemon License")
        input("Press Enter to continue")
        print("Zeus was so excited for his birthday tomorrow that he couldn't sleep.")
        input("Press Enter to continue")
        print("Cronos: Zeus! Get to sleep! You will need your strength for your big day tomorrow!")
        input("Press Enter to continue")
        print("Zeus: I realize that father, but I can't sleep!")
        input("Press Enter to continue")
        print("Chronos: I can understand that my child. I was the same way when I was turning 10 as well. How about this? Let's watch this on the TV until you are tired")
        input("Press Enter to continue")
        print("Chronos flips on the TV and Professor Hades can be seen on the screen with Bulbasaur, Squirtile and Charmander")
        input("Press Enter to continue")
        print("Prof. Hades: Good evening, Pallet. Tomorrow's a big day for the newest class of Pokemon students. Here i have Bulbasaur, Charmander, and Squirtle, each availablef or new trainers. WHich one shall you choose?...")
        input("Press Enter to continue")
        print("Zeus stays up all night watching the TV show, excited for the big day ahead")
        input("Press Enter to continue")
        print("As time passes, Zeus slowly falls asleep")
        input("Press Enter to continue")
        print("Some more time passes, and after a while Zeus wakes up groggily")
        input("Press Enter to continue")
        print("After a few seconds, Zeus looks at his alarm clock and realizes he never set his alarm")
        input("Press Enter to continue")
        print("Zeus: Oh no! I am late!")
        input("Press Enter to continue")
        print("Zeus rushes outside and onward towards Professor Hades' laboratory")
        input("Press Enter to continue")
        print("As Zeus reaches the laboratory, a large crowd dissipates from around the building, leaving Professor Hades alone at his door step")
        input("Press Enter to continue")
        print("Hades: Better late than never, Zeus! I am afraid I am out of pokemon to give away today. You will have to wait a few days for the next pokemon shipment to come in from the Underworld")
        input("Press Enter to continue")
        print("Zeus: Oh come on Professor! Surely you have one left! I can't wait another day for my first pokemon!")
        input("Press Enter to continue")
        print("Hades: Hmm, well we do have one more pokemon, but I am afraid that he is a bit aggressive")
        input("Press Enter to continue")
        print("Zeus: That sounds perfect professor! I'll take it!")
        input("Press Enter to continue")
        print("Hades: Well in that case, here you go...")
        input("Press Enter to continue")
        print("Standing on the ground next to the professor was a small pokemon with human-like features")
        input("Press Enter to continue")
        print("Pokemon: HERCU, HERC!")
        input("Press Enter to continue")
        print("Hades: His name is Hercules.")
        input("Press Enter to continue")
        print("Zeus: He is perfect!")
        input("Press Enter to continue")
        print("Zeus reaches down to give Hercules a hug and Hercules doesn't look happy as Zeus approaches")
        input("Press Enter to continue")
        print("Hercules: HERCU...LEEEEES")
        input("Press Enter to continue")
        print("Zeus writhes in different directions as he is shocked by the Hercules")
        input("Press Enter to continue")
        print("Hades: I told you, you gotta watch out. Hercules has an electrifying personality.")
        input("Press Enter to continue")
        print("Zeus: I see what you mean Professor")
        input("Press Enter to continue")
        print("Suddenly, the door to the laboratory swings open and a large figure appears in the doorway")
        input("Press Enter to continue")
        print("King Eurystheus: Hello young adventurer, I have need of your assistance")
        input("Press Enter to continue")
        print("Zeus and Hades both look at the man who just walked into the doorway, confused at both his boldness and his strange attire")
        input("Press Enter to continue")
        print("Hades: Who are you? Also, what is with that outfit?")
        input("Press Enter to continue")
        print("King: There is no time to explain! I need this young man's help! Please use your new pokemon to defeat the three trials of the master!")
        input("Press Enter to continue")
        print("Zeus: Well you seem pretty adamant about it, I suppose I could help. What's in it for me?")
        input("Press Enter to continue")
        print("King: Nothing really")
        input("Press Enter to continue")
        print("Zeus: Well, a majority of us end up walking around this giant contintent with nothing anyways, I suppose this isn't very different. What are the tasks?")
        input("Press Enter to continue")
        print("King: I need you to kill the Nemean Lion, defeat the impossible nine-headed Lernaean Hydra, and capture Cerberus!")
        input("Press Enter to continue")
        print("Hades: Now hold on a second, Cerberus is my pokemon and spends most of his day outback basking in the sun. He wouldn't hurt a fly!")
        input("Press Enter to continue")
        print("Hades: Zeus, I don't like this guy, I dont think you should help him")
        input("Press Enter to continue")
        print("Zeus: Oh c'mon gramps, this sounds like the perfect beginning to my pokemon adventure!")
        input("Press Enter to continue")
        print("Hades tries to reach out to get Zeus' attention, but it is too late as Zeus has headed through the door and onwards towards his first pokemon adventure!")
        print("Intro complete")
        input("Press Enter to continue")


    def nem_lion(self):
        print("As Zeus wanders around in the woods nearby Pallet Town with Hercules in tow, he is whispering to himself")
        input("Press Enter to continue")
        print("Zeus: I really shouldn't have run off without asking for directions first.")
        input("Press Enter to continue")
        print("As Zeus looks around, he sees something that looks like a rack of lamb, hanging from a string...in the middle of the woods")
        input("Press Enter to continue")
        print("Zeus: Oh Boy! Just what I needed! I am so hungry from walking around in these woods!")
        input("Press Enter to continue")
        print("Hercules reaches out to try to stop Zeus but its too late. Zeus grabs onto the lamb.")
        input("Press Enter to continue")
        print("Immediately, the ground underneath Zeus disappears and Zeus falls into a pitfall")
        input("Press Enter to continue")
        print("Hercules rushes over to the hole and looks inside to see Zeus incapacitated on the ground")
        input("Press Enter to continue")
        print("Soon after rushing over to see if Zeus was ok, a monster hops out from behind a bush!")
        input("Press Enter to continue\n")
        self.battle_one = Battlefield(1)
        self.battle_one.run_match()
        self.choose_reward()
        print("\nGah! The surprise enemy yells as he is beaten")
        input("Press Enter to continue")
        print("Zeus crawls out of the hole, and lays down at the top of the hole for a second, catching his breathe")
        input("Press Enter to continue")
        print("Great job Hercules! You really showed that Goblin who was boss!")
        input("Press Enter to continue")
        print("Suddenly, an animal jumps out from behind another bush!")
        input("Press Enter to continue\n")
        self.battle_two = Battlefield(2)
        self.battle_two.run_match()
        self.choose_reward()
        print("\nZeus: Great hit Hercules, but we have to get out of here before we get swarmed by more of those pokemon!")
        input("Press Enter to continue")
        print("Zeus and Hercules hurry out of the woods as fast as they can, trying to get away before any more goblins appear")
        input("Press Enter to continue")
        print("Eventually, they stumble out of the woods and into a clearing")
        input("Press Enter to continue")
        print("In the middle of the clearing is a giant statue of a lion")
        input("Press Enter to continue")
        print("Zeus: Whoa Hercules! We must be close to the Nemeaen Lion that that guy was talking about!")
        input("Press Enter to continue")
        print("The pair walk slowly up to the statue, wary that more goblins might be just around the corner")
        input("Press Enter to continue")
        print("Goblin Attack! They were not wary enough!")
        input("Press Enter to continue\n")
        self.battle_one = Battlefield(1)
        self.battle_one.run_match()
        self.choose_reward()
        print("\nOk, these goblins have to stop attack us, this is getting kind of old")
        input("Press Enter to continue")
        print("Zeus did not realize, but during the scuffle between Hercules and the Goblin, the statue had come to life!")
        input("Press Enter to continue")
        print("Nemeaeaeaen Lion attack!")
        input("Press Enter to continue\n")
        self.battle_four = Battlefield(4)
        self.battle_four.run_match()
        self.choose_reward()
        self.choose_reward()
        print("\nThe pair successful defeated the Nemeaeeaeaeaean Lion!")
        input("Press Enter to continue")
        print("Zeus: Great job Hercules!")
        input("Press Enter to continue")
        print("Hercules: HERCULES!")
        input("Press Enter to continue")
        print("The Nemeaen Saga has concluded\n")


    def lern_hydra(self):
        print("After taking a second to breathe after all of the excitement, the dynamic duo continue their journey to the Indigo Plataeu")
        input("Press Enter to continue")
        print("They look accross the clearing and see a far away plateau and what looks like a nine-headed Lernaean Hydra on top of it")
        input("Press Enter to continue")
        print("Zeus: Let's head that way!")
        input("Press Enter to continue")
        print("The duo make their way to the Lernaeaean Hydra, stepping accross various shrubberies along the grassy field")
        input("Press Enter to continue")
        print("After stepping over a particularly precarious set of bushes, an animal jumps out!")
        input("Press Enter to continue\n")
        self.battle_two = Battlefield(2)
        self.battle_two.run_match()
        self.choose_reward()
        print("\nZeus: Watch out Hercules, we gotta be more careful")
        input("Press Enter to continue")
        print("Hercules: I do agree, my good sir.")
        input("Press Enter to continue")
        print("They walk further towards the plateau when a set of goblins attacks Hercules in a single-file line")
        input("Press Enter to continue")
        print("Zeus: Ah! Watch out! They have learned how to attack in formation!")
        input("Press Enter to continue\n")
        self.battle_one = Battlefield(1)
        self.battle_one.run_match()
        self.battle_one = Battlefield(1)
        self.battle_one.run_match()
        self.choose_reward()
        print("\nThe programmed protagonists are almost at the base of the plateau!")
        input("Press Enter to continue")
        print("As they get closer and closer, the Hydra gets larger and larger")
        input("Press Enter to continue")
        print("Zeus: That Hydra really is large! I think I count 8 heads!")
        input("Press Enter to continue")
        print("Hercules: Hercules!")
        input("Press Enter to continue")
        print("As they finally arrive at the base of the plateau, they can see that the plateau protrudes over a cliffside")
        input("Press Enter to continue")
        input("The Hydra and all nine of his heads takes notice")
        input("Press Enter to continue")
        print("The Hydra heaves his gigantic body and all nine of his heads off of the plateue and in front of the adventurers")
        input("Press Enter to continue")
        print("Hydra Attack!")
        input("Press Enter to continue\n")
        self.battle_five = Battlefield(5)
        self.battle_five.run_match()
        self.choose_reward()
        self.choose_reward()
        print("\n Hercules is victorious against the Hydra, but the ground begins to shake as the plateau falls into the cliffside")
        input("Press Enter to continue")
        print("The ground beneath the duo starts to contort as a small fissure snakes from the cliff to the adventurers")
        input("Press Enter to continue")
        print("Zeus: Oh no! Run Hercules!")
        input("Press Enter to continue")
        print("Hercules: Hercules!")
        input("Press Enter to continue")
        print("Quickly, Zeus and Hercules run away from the cliffside, but the quake was too quick")
        input("Press Enter to continue")
        print("Zeus and Hercules: AAAHHHH!")
        input("Press Enter to continue")
        print("The ground falls away into the cliffside, taking the adventurers with it who pass out almost immediately")
        input("Press Enter to continue")
        print("That was the end of the Lernaean Hydra.")

    def cerb(self):
        print("While being swept to the bottom of the cliff along the landslide, the pair ended up in a dark and dusty area, with only the moonlight shining in from the top of the cliff illuminating their surroundings")
        input("Press Enter to continue")
        print("The adventurers wake up to see that some time has passed, Zeus stands up to take a look around")
        input("Press Enter to continue")
        print("Zeus: Let's take a look around Hercules, surely this place is safe after such a massive landslide")
        input("Press Enter to continue")
        print("After climbing down from the rubble, the two take a few steps into the dark and are immediately attacked")
        input("Press Enter to continue")
        print("Zeus: Oh no! What is this thing?")
        input("Press Enter to continue\n")
        self.battle_three = Battlefield(3)
        self.battle_three.run_match()
        self.choose_reward()
        print("\nZeus: Hercules, I told you to be careful, we don't know what is around here!")
        input("Press Enter to continue")
        print("Hercules punches Zeus in the side of his leg")
        input("Press Enter to continue")
        print("Zeus: Hey! What was that for?...... Oh no! Watch out! More of them!")
        input("Press Enter to continue")
        print("Once again in formation, more monsters attack the duo")
        input("Press Enter to continue\n")
        self.battle_three = Battlefield(3)
        self.battle_three.run_match()
        self.battle_three = Battlefield(3)
        self.battle_three.run_match()
        self.battle_three = Battlefield(3)
        self.battle_three.run_match()
        self.choose_reward()
        print("\nAfter barely defeating the wave of monsters, a familiar voice can be heard from the shadows")
        input("Press Enter to continue")
        print("Hades: You guys really couldn't just sleep in today could you?")
        input("Press Enter to continue")
        print("Zeus: Hades?")
        input("Press Enter to continue")
        print("Hercules: Hades?!?")
        input("Press Enter to continue")
        print("Hades: I go through all of this trouble rewriting reality based on my favorite anime, and you two couldn't just leave well enough alone")
        input("Press Enter to continue")
        print("Zeus: What are you even talking about Hades? What is an anime?")
        input("Press Enter to continue")
        print("Hades: It's no matter, I have the strongest pokemon in the world. Cerberus! Sick'em boy!")
        input("Press Enter to continue")
        print("The giant three-headed dog from the village launches from the shadows on a collision course for Zeus")
        input("Press Enter to continue")
        print("Hercules jumps in front of Zeus and deflects the giant dog, protecting Zeus")
        input("Press Enter to continue")
        print("Cerberus Attack!")
        input("Press Enter to continue\n")
        self.battle_six = Battlefield(6)
        self.battle_six.run_match()
        print("\n Zeus: Now is my chance!")
        input("Press Enter to continue")
        print("With all of his might, Zeus throws a masterball at Cerberus")
        input("Press Enter to continue")
        print("Hades: Whoa bro! It's not cool to catch someone else's pokemon!")
        input("Press Enter to continue")
        print("Unsurprisingly, the ball rocks three times and blinks to show that Cerberus has been caught")
        input("Press Enter to continue")
        print("A random explosion launches Hades upwards, out of the cliff after Cerberus is captured")
        input("Press Enter to continue")
        print("Hades: Team Hades is blasting off again!")
        input("Press Enter to continue")
        print("The Cerberus has been captured")
        input("Press Enter to continue")


    def end(self):
        print("Zeus and Hercules have defeated the three trials of King Eurystheus")
        input("Press Enter to continue")
        print("Congratulations! You have beaten the game!")
