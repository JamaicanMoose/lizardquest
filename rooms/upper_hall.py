from items.item import Item
from items.mixins import Entrance, Fixed, Readable

""" The Upper Hallway
"""

class doubleDoors(Entrance, Item):
    name = 'double doors'
    entrance_destination = 'bridge'
    description = ('A set of double doors leading to the BRIDGE.')

class officeDoor(Entrance, Item):
    name = 'office door'
    entrance_destination = 'HAOoBaM'
    description = ('A door to a side office.')

class stairsDown(Entrance, Item):
    name = 'stairs down'
    entrance_destination = 'stairwell'
    description = ('A set of stairs going back down.')

_lizard = 'A stunning portrait of a green lizard mottled with dark spots.'

class lizardPainting(Fixed, Readable, Item):
    name = 'lizard painting'
    alt_names = ['painting']
    description = _lizard
    text = ('𝘓𝘪𝘻𝘢𝘳𝘥, artist unknown. Oil on canvas.')

_upper_hall_desc = '''\
You are in the UPPER HALLWAY.
There is a GRAND STAIRCASE heading DOWN.
A bureaucratic-looking office door is labeled "HAOoBaM."
There is another door to the NORTH leading to the BRIDGE.
'''

upper_hall = {
    'description': _upper_hall_desc,
    'items': [lizardPainting()],
    'people': [],
    'exits': {
        'north': doubleDoors(),
        'workwards': officeDoor(),
        'down': stairsDown(),
    }
}
