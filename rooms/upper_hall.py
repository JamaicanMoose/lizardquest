from items.item import Item
from items.mixins import Entrance, Fixed, Readable, Lockable, Openable
from errors import CommandFailed
from time import sleep

""" The Upper Hallway
"""

class DoorToRoom(Lockable, Openable, Entrance, Item):
    name='door'
    alt_names = ['room', 'west']
    entrance_destination = None
    entrance_destination_name = 'room'
    entrance_type = 'door'
    lockable_locked = True
    openable_open = False
    description = ''

    def examine(self):
        Entrance.examine(self)
        print('''\
An extremely sturdy metal door with its lock destroyed.'''
        )
        print('''\
You can\'t see why someone would brerak the lock, it\'s just a normal looking
door to a normal seeming room.'''
        )
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('''\
As you begin to turn away, something seems to move in the corner of your eye.
For the briefest second, you could swear you saw through the door.
And on the other side...'''
        )
        sleep(5)
        print('Movement?')
        sleep(1.5)
        print('Blood?')
        sleep(1.5)
        print('Teeth?')
        sleep(1.5)
        print('''\
Whatever it was, it certainly wasn\'t a normal body, and that certainly
wasn\'t a normal Room.'''
        )
        sleep(1.5)
        print('''\
There is a soft scratching coming from the other side, and you\'re
glad the lock is engaged.'''
        )
        sleep(1.5)
        print('''\
You understand why the Room. is off limits.'''
        )
        sleep(1.5)
        print('''\
You suddenly understand what it took to close it.'''
        )
        sleep(1.5)
        print('''\
The sacrifices that were made.'''
        )
        sleep(1.5)
        print('''\
You won\'t forget. You can\'t forget.'''
        )
        sleep(1.5)
        print('''\
You turn around to leave and-'''
        )
        sleep(1.5)
        print('''\
huh.'''
        )
        sleep(1)
        print('''\
That\'s weird.'''
        )
        sleep(1.5)
        print('''\
There are tears on your cheeks!'''
        )
        sleep(1.5)
        print('''\
You can\'t remember seeing anything that sad recently... weird.'''
        )
        sleep(2)
        print('There is a small label on the door.')

    def unlock(self):
        print('''\
The lock on the door is completely destroyed.
It looks like this was done intentionally.'''
        )
        raise CommandFailed()


class DoorsToBridge(Entrance, Item):
    name = 'double doors'
    alt_names = ['north']
    entrance_destination = 'bridge'
    entrance_destination_name = 'bridge'
    entrance_type = 'double doors'
    description = '''\
A large set of double doors.

The left one has a small label on it.'''


class DoorToOffice(Entrance, Item):
    name = 'door'
    alt_names = ['north east']
    entrance_destination = 'HAOoBaM'
    entrance_destination_name = 'office'
    entrance_type = 'door'
    description = '''\
A large bureaucratic looking door labeled \"HAOoBaM\".
You peer through the porthole and see a very plain office.

It has a small label on it.'''


class StaircaseToStairwell(Entrance, Item):
    name = 'staircase'
    alt_names = ['south', 'grand staircase', 'stairs']
    entrance_destination = 'stairwell'
    entrance_destination_name = 'stairwell'
    entrance_type = 'staircase'
    description = '''\
A grand staircase that lead downwards.

At your feet is a small label.'''


class lizardPainting(Fixed, Readable, Item):
    name = 'lizard painting'
    alt_names = ['painting']
    description = '''\
A stunning portrait of a green lizard mottled with dark spots.'''
    text = ('𝘓𝘪𝘻𝘢𝘳𝘥, artist unknown. Oil on canvas.')


upper_hall = {
    'description': '''\
You are in the UPPER HALLWAY.
''',
    'items': [
        lizardPainting()
    ],
    'people': [],
    'exits': {
        'north': DoorsToBridge(),
        'north east': DoorToOffice(),
        'south': StaircaseToStairwell(),
        'west': DoorToRoom()
    }
}
