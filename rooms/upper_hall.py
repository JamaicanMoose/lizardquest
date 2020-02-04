from items.item import Item
from items.mixins import Entrance

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

upper_hall = {
    'description': ('You are in the UPPER HALLWAY.'),
    'items': [],
    'people': [],
    'exits': {
        'north': doubleDoors(),
        'workwards': officeDoor(),
        'down': stairsDown(),
    }
}
