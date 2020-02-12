from items.item import Item
from items.mixins import Entrance, Fixed
from scenarios.scenario import Scenario
from time import sleep
from person import Person
""" The Zen Garden
"""

class ArchWayToRecRoom(Entrance, Item):
    name = 'archway'
    alt_names = ['east']
    entrance_destination = 'recRoom'
    entrance_destination_name = 'rec room'
    entrance_type = 'archway'
    description = '''\
An ornate stone archway.
Through the archway you see the rec room.

There is a small label on it.'''

class LadderToEscapePods(Entrance, Item):
    name = 'ladder'
    alt_names = ['down']
    entrance_destination = 'escapePods'
    entrance_destination_name = 'escape pods'
    description = '''\
A sturdy chrome ladder.
Looking downwards you see pristine white floors.

There is a small label on it.'''

class Bonsai(Fixed, Item):
    name = 'bonsai'
    alt_names = ['tree', 'bonsai tree']
    description = ('The well-manicured bonsai tree sticks out from beneath '
                   'the stones at your feet, its roots out of sight.\nThe '
                   'tree itself resembles a cherry blossom, only smaller.\n'
                   'Despite the impeccable appearance of the tree, there is '
                   'no gardener in sight.')
    take_fail_text = '''\
Taking the bonsai would likely disturb the pristine nature of the room, so
it's probably best not to take it. Besides, it would probably be unwieldy.'''

class KoiConversation(Scenario):

    def alt_convo(self, state):
        print("You attempt to speak to the fish, but no voice responds. "
              "Instead, you feel their presence in your mind--powerful, "
              "prudent, and eternal.")
        return

    def start(self, state):
        if '_koi_questioned' in _game_state:
            self.alt_convo(state)
            return

        print("As you attempt to converse with the fish, you are taken aback "
              "as a voice fills your mind!")
        sleep(1)
        print("\"Hello,\" utters the harmonious voice, the voice of three "
              "beings projecting their thoughts in unison.")
        sleep(1)
        print("\"We are the three koi. We have dwelled in this garden "
              "since before it was a garden, and we will do so until long "
              "after it has shed its present form.\"")
        sleep(1)
        print("Cherry blossom leaves drift from the bonsai onto the surface "
              "of the pool.")
        sleep(1)

        print("\"We will answer one question that you have. What would you "
              "ask?\"")
        choice = Scenario.pick(["Where am I?", "Is a hot dog a sandwich?",
                                "How much wood would a woodchuck chuck if a " +
                                "woodchuck could chuck wood?"])

        print("The voice briefly stops, pondering your question.")
        sleep(2)
        if choice == 0:
            print("\"You are aboard a spaceship, the NATTIC, or the "
                  "FriendShip™ Navigational Tool and Travel Companion, version "
                  "2.6, which is manned by a crew of intergalactic "
                  "adventurers.\"")
        elif choice == 1:
            print("\"Let it be so.\"")
            print("And then, as if with the snap of a finger, all hot dogs "
                  "that are, were, or ever will be, became sandwiches.")
        else:
            print("\"A woodchuck would chuck as much wood as a woodchuck "
                  "could chuck if a woodchuck could chuck wood.\"")

        _game_state['_koi_questioned'] = True
        _game_state['player'].add_accolade('The Harmonious')

class Fish(Person):
    name = 'koi'
    alt_names = ['fish', 'koi fish']
    description = ("The three koi fish are all different colors: one is gold, "
                   "one is black, one is white.\nThey swim around in peace, "
                   "seemingly unaware that even as they rest, they are "
                   "hurtling lightyears through the universe in a "
                   "chrome-plated spaceship.")
    scenario = KoiConversation()

zen_garden = {
    'description': '''
A feeling of ease flows over you.
The floor is covered in grass and well-rounded stones, and a BONSAI TREE
sticks out from them.
A pool of KOI FISH lies below the tree\'s branches.''',
    'items': [
        Bonsai()
    ],
    'people': [
        Fish()
    ],
    'exits': {
        'north': ArchWayToRecRoom(),
        'down': LadderToEscapePods(),
    }
}
