from items.item import Item
from items.mixins import Entrance
from scenarios.scenario import Scenario
from person import Person
from util import endgame
from time import sleep

""" The Herpetology Room [Room (0,0,0)]
"""

class DoorsToUpperHall(Entrance, Item):
    name = 'double doors'
    alt_names = ['south']
    entrance_destination = 'upperHall'
    entrance_destination_name = 'upper hall'
    entrance_type = 'double doors'
    description = '''\
A large set of double doors.

The left one has a small label on it.'''


class LadderToCaptainsRoom(Entrance, Item):
    name = 'ladder'
    alt_names = ['down']
    entrance_destination = 'captainsRoom'
    entrance_destination_name = 'captain\'s room'
    entrance_type = 'ladder'
    description = '''\
A ladder.
Looking down you can see the carpet on the floor.

The ladder has a small label on it.'''


class consolationLizard(Item):
    name='consolation lizard'
    prettyname='A Consolation Lizard'
    alt_names=['lizard', 'bad lizard']
    description="The lizard looks at you with judgement and pity in its eyes.\nIt shakes its head, slowly."


class natticConversation(Scenario):
    hasntmet = True
    accoladeCount = 0
    askedForFriend=False


    def start(self, bridgeComputer):
        def nsay(text):
            print(f'NATTIC : \"', end='')
            print(text, end='')
            print(f'\"')

        def anything_else():
            nsay('''\
Was there anything else you needed?'''
            )

        def _n():

            choices = []
            if self.askedForFriend==False:
                choices.append(('Hey there! I\'m looking for a friend!', _evaluateFirst,))
            elif self.askedForFriend==True:
                choices.append(('Can you check my accolades again?', _evaluate,))
            choices.append(('Tell me more about yourself!', _about,))
            choices.append(('Do you have any information about the ship?', _aboutShip,))
            choices.append(('~SV_CHEATS 1', _enableCheats,))
            choices.append(('Evaluate: This sentence is false', _paradox,))
            choices.append(('Input new travel destination', _travel,))
            choices.append(('[ACTION] Give Nattic a hug', _hug))
            Scenario.choose(choices)

        def _evaluate():
            self.accoladeCount=0
            nsay('''\
Alright, let's see what you've been up to!
''')
            if _game_state['player'].has_accolade("The Hungry"):
                print("\nEVALUATING: The Hungry\n")
                nsay("Aw gosh! They didn't even feed you? Aw shucks.\nwell, hey! Y'know what they say- hungry is a synonym for ambitious! ")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_accolade("The Trapped"):
                print("\nEVALUATING: The Trapped\n")
                nsay("Oooh... a bit of a broody type, are we? That's okay.\nWe all have our barriers we put up.\nI'm here for ya.")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_accolade("The Lonely"):
                print("EVALUATING: The Lonely")
                nsay("Oh jeez! Hopefully not for long!")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_accolade("Printer Of Labels"):
                print("\nEVALUATING: Printer Of Labels\n")
                nsay("That's... I guess that's something?\nAt the very least, it proves you know how to use a labelmaker.")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_accolade("Cares About Others"):
                print("\nEVALUATING: Cares About Others\n")
                nsay("Awwwwh! That's so sweet! I knew you had a heart of gold, you big softy, you!")
                self.accoladeCount=self.accoladeCount+3
                sleep(1.5)

            if _game_state['player'].has_accolade("The Triangular"):
                print("\nEVALUATING: Triangular\n")
                nsay("You're a triangular-sandwich sort of person, huh?")
                print("Nattic nods, their expression unreadable.")
                nsay("That explains a lot.")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_accolade("The Rectangular"):
                print("\nEVALUATING: Rectangular\n")
                nsay("You're a rectangular-sandwich sort of person, huh?")
                print("Nattic nods, their expression unreadable.")
                nsay("That explains a lot.")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_accolade("The Harmonious"):
                print("\nEVALUATING: The Harmonious\n")
                nsay("Harmonious, eh?\nHmmm.. something seems FISHY about this one!\nI'm just kidding! That's a really wonderful trait!")
                self.accoladeCount=self.accoladeCount+3
                sleep(1.5)

            if _game_state['player'].has_title("Epicureous"):
                print("\nEVALUATING: The Epicureous\n")
                nsay("Hey, you're making your way up in the world!\nAnd by \"your way up in the world\", I mean \"a sandwich\"!")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_accolade("The Conscientious"):
                print("\nEVALUATING: The Conscientious\n")
                nsay("Look at you! So kind and considerate!\nWas that something you learned, or were you... BREAD that way?")
                self.accoladeCount=self.accoladeCount+3
                sleep(1.5)

            if _game_state['player'].has_accolade("Captured But Free"):
                print("\nEVALUATING: Captured But Free\n")
                nsay("That's a rad name. Right on, right on.")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_accolade("Big Fat Liar"):
                print("\nEVALUATING: Big Fat Liar\n")
                nsay("Um... hey, not gonna lie, this one's pretty bad.")
                self.accoladeCount=self.accoladeCount-1
                sleep(1.5)

            if _game_state['player'].has_accolade("The Studious"):
                print("\nEVALUATING: The Studious\n")
                nsay("Sounds like it's time to hit the books!\nGood luck on that test.")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)


            if _game_state['player'].has_accolade("The Generous"):
                print("\nEVALUATING: The Generous\n")
                nsay('After all that... you gave the sandwich away?\nW...Wow.\n[Nattic tears up a bit, as much as it\'s possible for a projection to cry]\nThat\'s moving, it really is.')
                self.accoladeCount=self.accoladeCount+4
                sleep(1.5)

            if _game_state['player'].has_title("Lizard Archwizard"):
                print("\nEVALUATING: Lizard Archwizard\n")
                nsay("You... hang on. I've got a list of all the Lizard Archwizards, and... you aren't on it.\nYou couldn\'t...You wouldn\'t... how DARE you sully the name of the Lizard Wizards!")
                self.accoladeCount=self.accoladeCount-2
                sleep(1.5)

            if _game_state['player'].has_accolade("Lizard Apprentice"):
                print("\nEVALUATING: Lizard apprentice\n")
                nsay("Congratulations! But... does this mean you'll be leaving soon?")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_accolade("Rude Talker"):
                print("\nEVALUATING: Rude Talker\n")
                nsay("Hey. Be nice.")
                self.accoladeCount=self.accoladeCount-1
                sleep(1.5)

            if _game_state['player'].has_accolade("Affectionate to a fault"):
                print("\nEVALUATING: Affectionate to a fault\n")
                nsay("Even though you knocked the ship .5 degrees off course, it was a very sweet gesture.")
                self.accoladeCount=self.accoladeCount+3
                sleep(1.5)

            if _game_state['player'].has_title("Mad"):
                print("\nEVALUATING: Mad\n")
                print("Nattic shifts their projection to look like a hockey player being interviewed.")
                nsay("Iss only game. Why you heff to be mad?")
                print("Nattic shifts back to their usual projection, just rendering an emoticon face.")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_title("Iron Chef"):
                print("\nEVALUATING: Iron Chef\n")
                nsay("Iron Chef? That's pretty vintage.\nMost folks are into Osmium Chef these days.")
                self.accoladeCount=self.accoladeCount+1
                sleep(1.5)

            if _game_state['player'].has_title("Fashion Criminal"):
                print("\nEVALUATING: Fashion Criminal\n")
                nsay("Did you... steal those clothes? I mean... they do look nice.")
                self.accoladeCount=self.accoladeCount+0
                sleep(1.5)

            if _game_state['player'].has_title("Puzzle Solver Extraordinaire"):
                print("\nEVALUATING: Puzzle Solver Extraordinaire\n")
                nsay("WOAH! Am I... in the presence of a puzzle master? Amazing work!")
                self.accoladeCount=self.accoladeCount+2
                sleep(1.5)

            print('EVALUATION COMPLETE. YOUR FRIENDSHIP SCORE IS: '+str(self.accoladeCount())+'.')

            if accoladeCount>20:
                nsay('''\
Wow! You... actually did it!
The trials were tough, but you pulled through.
I'm proud of you, and I'd be more than happy to call you my friend.
Pull up a chair - Let's just sit and talk for a while.
It's been ages since I've had someone that I can chat with,
without having to worry about their health and safety.
''')
                if not _game_state['player'].has_accolade('The Ultimate Friend'):
                    _game_state['player'].add_accolade('The Ultimate Friend')
                if _game_state['player'].has_accolade('The Lonely'):
                    print("The two of you sit and talk for a long, long while.")
                    sleep(1)
                    print('''\
... time passes. You get to know the folks on board the ship.
''')
                    sleep(1)
                    print('''\
Over time, they consider you a member of the family. You move into one of the empty dorms.
''')
                    sleep(1.5)
                    print('''\
When you finally arrive at the next spaceport, you decide to stick around on the ship, rather than leaving.
''')
                    sleep(1.5)
                    print('''\
You're no longer lonely- from that day forward, your days are spent with those you love.
''')
                    sleep(2)
                    endgame()
                else:
                    print("You have a really nice conversation with Nattic!\nAfterwards, you get up and continue on your way.")
                    nsay("Good luck on your quest!")
            elif accoladeCount>12:
                ##END GAME, GOOD END
                nsay('''\
Wow! You... actually did it!
The trials were tough, but you pulled through.
I'm proud of you, and I'd be more than happy to call you my friend.
Pull up a chair - Let's just sit and talk for a while.
It's been ages since I've had someone that I can chat with,
without having to worry about their health and safety.
''')
                if not _game_state['player'].has_accolade('Worthy of Friend Ship'):
                    _game_state['player'].add_accolade('Worthy of Friend Ship')
                if _game_state['player'].has_accolade('The Lonely'):
                    print("The two of you sit and talk for a long, long while.")
                    sleep(1)
                    print('''\
... time passes. You get to know the folks on board the ship.
''')
                    sleep(1)
                    print('''\
Over time, they consider you a member of the family. You move into one of the empty dorms.
''')
                    sleep(1.5)
                    print('''\
When you finally arrive at the next spaceport, you decide to stick around on the ship, rather than leaving.
''')
                    sleep(1.5)
                    print('''\
You're no longer lonely- from that day forward, your days are spent with those you love.
''')
                    sleep(2)
                    endgame()
                else:
                    print("You have a really nice conversation with Nattic!\nAfterwards, you get up and continue on your way.")
                    nsay("Good luck on your quest!")

            elif accoladeCount>5:
                nsay("You're well on your way! Keep up the good work!")
            elif accoladeCount>0:
                nsay("You've still got a ways to go, but I believe in you!")
            else:
                nsay("Somehow, you earned... negative friendship points?\nHey, take this lizard and get off my ship.")
                _game_state['player'].state['inventory'].append(consolationLizard())
                print('You take the consolation lizard.')

            anything_else()
            _n()

        def _evaluateFirst():
            askedForFriend=True
            nsay('''\
Oh, gosh, I'd love to be your friend, but... I don't really have the time to have to take care of another person!
Tell you what, though - if you can take care of yourself and help out around the ship,
and you've got the accolades and titles to prove it, then I'd be more than happy to be your friend.
''')
            _evaluate()
        def _about():
            nsay('''\
I'm Nattic! My full name is \"FriendShip-brand Navigational Tool and Travel Companion, v.2.6.3\",
but that's a mouthful, so I generally go by NTTC - hence, Nattic!
I'm installed onboard this ship to help stave off loneliness in the cold emptiness of space,
and to ensure that everyone onboard can travel safely among the stars!
''')
            anything_else()
            _n()

        def _aboutShip():
            nsay('''\
This ship, the Millenium Lizard, is bad in concept and worse in execution.
I don't have much else to say about it.
Who in their right mind powers their ship via space-lizards anymore?
Look, I have nothing but respect for the council of Lizard Wizards,
but it's like how the horse got replaced by the engine, you know?
''')

            print("\nYou don't know, but nod anyhow. What the space hell is a \"horse\"?")
            anything_else()
            _n()

        def _enableCheats():
            print("Nattic looks at you, quizzically.")
            nsay("Did you just pronounce a tilde? Out loud? With your mouth? How?")
            print("You shrug")
            nsay("In any case, I've already got valve anti-cheat. Nice try though!")
            anything_else()
            _n()
        def _paradox():
            print("Nattic sighs")
            nsay("No, it isn't. I know, it's a paradox. I'm not an idiot.")
            anything_else()
            _n()
        def _travel():
            nsay("Oh, sure! Where would you like to go?")
            r=str(input())
            nsay((r+" has been added to the travel queue.\nWe'll go there after reaching our current destination.\nETA: 5000 years or so."))
            nsay("Meanwhile, if you wanted to go somewhere onboard the ship, I suggest just... walking there.")
            anything_else()
            _n()
        def _hug():
            print('''\
You climb on top of the console to give Nattic a hug.
Your hands pass right through them, and you collapse onto the console, jostling a lever.
The whole ship lurches sharply to the left.

Nattic quickly rights the ship and projects themself down to you to see if you're okay.
''')
            nsay('''\
I appreciate the sentiment! But, um... next time, maybe just a high-five'll do.
''')
            if not _game_state['player'].has_accolade("Affectionate to a fault"):
                _game_state['player'].add_accolade("Affectionate to a fault")
            anything_else()
            _n()

        if self.hasntmet:
            nsay('''\
Oh! A new face!
Let's see here...
.'''
                 )
            sleep(1)
            nsay('''\
...That's strange, you aren't on the passenger registry.
Ah, well! No matter, I suppose! You're here now.
I'm Nattic, and I'm pleased as punch to meetcha!
I help keep things ship-shape around here.
''')
            self.hasntmet = False
        else:
            nsay('Oh, it\'s you! Come on in!')
        nsay('Was there something you needed?')
        _n()


class bridgeComputer(Person):
    name = 'bridge computer'
    alt_names = ['console','computer','friendship','ship','friend','nattic','Nattic','NTTC','nttc','friend ship','bridge']
    description = '''\
An installation of FriendShip(tm) Navigational Tool and Travel Companion, v2.6.3.
They're currently displaying a projection of a friendly, smiling face.
As they notice you staring, they make a few funny faces, then laugh a bit at themself.'''
    scenario = natticConversation()


bridge = {
    'description': ('''\
You are in the BRIDGE of the ship.
This room has floor-to-celing windows, which give an absolutely astonishing view of the stars.
The central BRIDGE COMPUTER gives off a flickering cyan projection, which switches images every so often-
from a humanoid figure, looking out the windows with a projection of a telescope,
to an emoticon, answering various issues and requests being sent in by the pirates,
to various navigational tools - sextants, compasses, and the like, all scribbling away and creating a
steady stream of data that flows across the l.e.d. tracers and circuit-patterns that run along the floor.

As for exits, there is a LADDER to the captain\'s room and a large DOOR back into the upper hallway.
'''),
    'items': [],
    'people': [bridgeComputer()],
    'exits': {
        'south': DoorsToUpperHall(),
        'down': LadderToCaptainsRoom(),
    }
}
