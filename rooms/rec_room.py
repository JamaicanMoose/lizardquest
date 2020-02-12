from items.item import Item
from items.mixins import Entrance, Fixed, Readable, Lockable, Openable
from errors import CommandFailed
from time import sleep

""" RecRoom
"""

class LadderToBrig(Entrance, Item):
    name = 'chrome ladder'
    alt_names = ['ladder', 'down']
    entrance_destination = 'brig'
    entrance_destination_name = 'brig'
    entrance_type = 'ladder'
    description = '''\
A sturdy chrome ladder.
Looking downwards you see the dim lit brig where you came from.

There is a small label on it.'''


class DoorToHerpetologyRoom(Entrance, Item):
    name = 'door'
    alt_names = ['east']
    entrance_destination = 'herpetologyRoom'
    entrance_destination_name = 'herpetology lab'
    entrance_type = 'door'
    description = '''
A large metal door.
The porthole is all fogged up.

There is a small label on it.'''


class DoorToDorms(Entrance, Item):
    name = 'door'
    alt_names = ['south']
    entrance_destination = 'dorms'
    entrance_destination_name = 'dorms'
    entrance_type = 'door'
    description = '''
A metal door.

There is a small label on it.'''


class ArchwayToZenGarden(Entrance, Item):
    name = 'archway'
    alt_names = ['west']
    entrance_destination = 'zenGarden'
    entrance_destination_name = 'zen garden'
    entrance_type = 'archway'
    description = '''\
An ornate stone archway that looks out of place against the metal of the ship.
Through the archway you see a lush green garden.

There is a small label on it.'''


class StaircaseToStairwell(Entrance, Item):
    name = 'staircase'
    alt_names = ['north', 'grand staircase', 'stairs']
    entrance_destination = 'stairwell'
    entrance_destination_name = 'stairwell'
    entrance_type = 'staircase'
    description = '''\
A grand staircase that lead upwards.

At your feet is a small label.'''


class DoorToKitchen(Entrance, Item):
    name = 'kitchen'
    alt_names = ['north west']
    entrance_destination = 'kitchen'
    entrance_destination_name = 'kitchen'
    entrance_type = 'door'
    description = '''\
A large metal door.
Through the porthole you can see a kitchen.

There is a small label on it.'''


class DoorToLizardBrothel(Openable, Entrance, Item):
    name='door'
    alt_names = ['lizard brothel', 'brothel', 'south east']
    entrance_destination = None
    entrance_destination_name = 'lizard brothel'
    entrance_type = 'door'
    openable_open = False
    description = '''\
A large metal door.
The porthole is blacked out so you can\'t see inside.

There is a small label on it.
The label has a tiny heart in red lipstick drawn on it.
'''

    def open(self):
        print('''\
Oh, no. You\'re not going in there.
Not after the incident at the last lizard brothel you went to.'''
        )
        raise CommandFailed()


class DoorToLizardRnD(Lockable, Openable, Entrance, Item):
    name='door'
    alt_names = ['south west']
    entrance_destination = None
    entrance_destination_name = 'lizard r&d'
    entrance_type = 'door'
    openable_open = False
    lockable_locked = True
    labjettisoned = False
    description = ''

    def examine(self):
        print('A large metal door.')
        if not self.labjettisoned:
            print('''\
There is a button next to the door labeled \"UNLOCK LATCHES\".'''
            )
            print('''\
Behind this door is the cutting edge of research into lizards
and lizard-care acoutrements.'''
            )
            sleep(2)
            print('''\
The door displays a holographic message:'''
            )
            sleep(1.5)
            print('''\
\"Testing in Progress. Do Not Disturb.\"'''
            )
            sleep(1.5)
            print('''\
From behind the door you can hear sounds of lasers and heavy machinery,
punctuated by the cheers of elated scientists.'''
            )
        else:
            print('''\
There is a button next to the door labeled
\"UNLOCK LATCHES IN CASE OF QUARANTINE\".'''
            )
            print('''\
No more sounds come from behind the door and through the porthole all you see
is the black nothingness of space.'''
            )
        sleep(2)
        print('There is a small label on it.')
        Entrance.examine(self)

    def unlock(self):
        if not self.labjettisoned:
            print('''You press the button labeled \"UNLOCK LATCHES\".''')
            sleep(1)
            print('''\
As you\'re pressing it a sticky note falls off and you see that the button
previously said \"UNLOCK LATCHES IN CASE OF QUARANTINE\".'''
            )
            sleep(2)
            print('CLUNK!')
            print('''\
You watch as the lab behind the door floats away into space.'''
            )
            sleep(2)
            print('''\
The scientists don\'t seem to notice.'''
            )
            sleep(2)
            _game_state['player'].add_title('Emergency Quarantine Officer')
            self.labjettisoned = True
        else:
            print('Thats not a mistake you want to revisit.')


class DoorToJustSoup(Lockable, Openable, Entrance, Item):
    name = 'door'
    alt_names = ['north east']
    entrance_destination = None
    entrance_destination_name = 'just soup'
    entrance_type = 'door'
    openable_open = False
    lockable_locked = True
    description = '''\
A large metal door plastered with the familiar branding of Just Soup,
a pretty mediocre chain restaurant.
A holo-screen informs you that the restaurant is currently closed for renovations.
Normally, when the restaurant is closed, you can order from the auto-vendor
attached to the outside window but the machine\'s display currently reads:
\"Error: Just Plain Broken\", which isn\'t the best inidicator of usability.
Ah, well. No big loss. You wanted a sandwich anyways.

There is a small label on the door.'''

    def unlock(self):
        print('You can\'t unlock it without the key!')
        raise CommandFailed()


class TVArea(Fixed, Item):
    name = 'TV area'
    description = '''\
An absolute monster of a couch is positioned in front
of an equally large television.
A stand of holo-discs sits nearby, and you quickly scan some of the titles
\"King of the Belly-button Piercing: Brotherhood of the Stud\"
\"We Legally Can\'t Call This Despicable Me\"
\"Star Wars Episode IV: A New Hope\"
that last one strikes you as odd.
Who would put a grim, serious documentary in with all these comedies?
In any case, you\'ve seen all these before, and don\'t really
feel like revisiting the classics.
You walk back to the center of the room.'''


rec_room = {
    'description': '''\
You are in the REC ROOM, also known as the RECREATION ROOM.
By far the largest room on the ship, it seems to serve as a sort of central hub of activity.
Holo-projectors create dazzling lightshows as smooth jazz plays over the speakers.
You can smell something delicious coming from the NORTH WEST door,
and you can hear the sounds of mist being sprayed beyond the EAST door.''',
    'items': [
        TVArea()
    ],
    'people': [],
    'exits': {
        'down': LadderToBrig(),
        'north': StaircaseToStairwell(),
        'east': DoorToHerpetologyRoom(),
        'north east': DoorToJustSoup(),
        'north west': DoorToKitchen(),
        'south east': DoorToLizardBrothel(),
        'south west': DoorToLizardRnD(),
        'south': DoorToDorms(),
        'west': ArchwayToZenGarden(),
    }
}
