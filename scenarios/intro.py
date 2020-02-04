from time import sleep
from .scenario import Scenario

def sleep(_n):
    pass

class GoalChoice(Scenario):
    def start(self, state):
        def _n():
            print("Finally free from your cell, you can now set your sights on "
                  "your ultimate goal.\nNow, what is that goal?")
            a = ('A tasty sandwich', _a)
            b = ('Escaping the spaceship', _b)
            c = ('A nice friend', _c)
            Scenario.choose([a,b,c])

        def _a():
            print("You hear a rumbling in your stomach, and, all of a sudden, "
                  "your ultimate goal becomes very apparent to you: a nice "
                  "sandwich!\nFree of the pirates' brig, you venture into the "
                  "ship's depths in search of such a treasure...")

        def _b():
            print("While you may be free from the cell, true freedom yet "
                  "eludes you: you're still stuck on this ship, hurtling "
                  "through the cosmos!\nAs such, your ultimate objective is "
                  "clear: find a means of escape to secure your future.\n"
                  "You head off into the depths of the ship in pursuit of "
                  "this goal...")

        def _c():
            print("You are now free of physical bonds, but you can't help "
                  "but think that this freedom would be so much more easily "
                  "enjoyed alongside a nice friend.\nFree of the jail cell's "
                  "steel bars, you head off into the ships' depths in search "
                  "of one of life's greatest treasures: friendship!")

        _n()

class Intro(Scenario):
    def start(self, state):
        def _n():
            print("You wake up. You're in a cold, metal-plated jail cell.\nIn your "
                  "cell is a small cot and table.\nOutside the bars of your cell, "
                  "there's a long hallway and someone who is probably your guard.")
            sleep(2)
            print("As your mind clears, you remember that you were kidnapped by "
                  "space pirates!\nThis must be their ship, and you are in "
                  "its brig.")
            sleep(2)
            print("What do you do?")
            a = ('Get the guard\'s attention', _a)
            b = ('Search the cell', _b)
            Scenario.choose([a,b])

        def _a():
            print("You whisper towards the guard.\nHe perks his head in "
                  "your direction, but then continues ignoring you.\nHow do "
                  "you get his attention?")
            a = ('Bribe him', _aa)
            b = ('Challenge him to a battle of wits', _ab)
            Scenario.choose([a,b])

        def _aa():
            print("A bit louder this time, you call for the guard, saying "
                  "that you can make it worth his while.\nThis seems to do "
                  "the trick, and he comes over to your cell.")
            sleep(2)
            print("The guard sleepily says, \"...and how're you gonna "
                  "do that?\"")
            a = ('Offer him a chance at a new life, '
                 'free of intergalactic crime', _aaa)
            b = ('Offer him astronaut ice cream', _aab)
            Scenario.choose([a,b])

        def _aaa():
            print("Offering the guard a spot at one of your relative's "
                  "space pilot training programs, a glimmer of hope "
                  "sparkles in his eye as he realizes a future where "
                  "he doesn't have to live outside the law.")
            sleep(2)
            print("He lets you out of the cell, and promises that he "
                  "won't tell anyone as long as you come back for him. "
                  "He says that he'll be waiting right here.")
            sleep(2)

        def _aab():
            print("\"I thought we were all out?\" the guard says, "
                  "as you pull a neat parcel of freeze-dried "
                  "dessert from your pocket.")
            sleep(2)
            print("As you hand it to the guard, he opens your cell "
                  "door and begins to hastily devour the astronaut "
                  "ice cream.")
            sleep(2)

        def _ab():
            print("You taunt the guard, saying that surely you can best "
                  "him in a battle of mental acuity.\nYour taunt is "
                  "successful, as he approaches you and challenges you to "
                  "a game of who can come up with the higher number.\n"
                  "Triumphantly, he gives the following number: "
                  "\"One trillion!\" How do you respond?")
            a = ('One trillion', _aba)
            b = ('Infinity', _abb)
            Scenario.choose([a,b])

        def _aba():
            print("After repeating his answer back to him, the guard "
                  "seems unsure who wins. Not wanting to seem like a "
                  "bad sport, he agrees to let you go, warning you "
                  "not to cause any trouble.")
            sleep(2)

        def _abb():
            print("After giving your answer, the guard is dumbstruck, "
                  "and it seems as if he had never thought about "
                  "the concept of infinity before. After a minute or "
                  "two of thinking, he shrugs his shoulders and lets "
                  "you free.")
            sleep(2)

        def _b():
            print("Do you want to search the cot or the table?")
            a = ('Search the cot', _ba)
            b = ('Search the table', _bb)
            Scenario.choose([a,b])

        def _ba():
            print("Searching the cot, you find a loose metal spring that "
                  "could feasibly be used as a lockpick.\nYou try it out "
                  "on the lock, managing to work it in to the mechanism.\n"
                  "Which way do you turn it?")
            a = ('Turn left', _baa)
            b = ('Turn right', _bab)
            Scenario.choose([a,b])

        def _baa():
            print("You turn left, the lock clicks, and the door "
                  "swings open.")
            sleep(2)
            print("The guard says \"I don't get paid enough to deal "
                  "with this,\" and turns away as if he didn't see "
                  "you break out of your cell.")
            sleep(2)

        def _bab():
            print("You turn right, and you hear a hideous and loud "
                  "clunking noise. After forcing it a bit, the lock "
                  "seems to break, and the homemade lockpick is stuck. "
                  "Fortunately for you, that seems to mean the door is "
                  "now open!")
            sleep(2)
            print("The guard says \"I don't get paid enough to deal "
                  "with this,\" and turns away as if he didn't see "
                  "you break out of your cell.")
            sleep(2)

        def _bb():
            print("On the table, you find a conveniently-placed shrinkray!\n"
                  "What do you do with it?")
            a = ('Shrink yourself to fit through the door', _bba)
            b = ('Threaten to shrink the guard', _bbb)
            Scenario.choose([a,b])

        def _bba():
            print("You shrink yourself, and the shrinkray clatters to "
                  "the floor broken.\nYou now stand at probably an inch or so "
                  "tall, and you're free to leave unimpeded!")
            sleep(2)
            print("Shortly after leaving the cell, you find yourself "
                  "slowly regrowing.\nBefore you know it, you're back "
                  "to normal size!")
            sleep(2)

        def _bbb():
            print("You tell the guard that unless he lets you go, "
                  "you'll shrink him!\nHe very readily agrees, and he "
                  "opens the door to your cell.\nYou're free to go!")
            sleep(2)

        _n()
        GoalChoice().start(state)
