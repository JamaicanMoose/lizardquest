from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Upper Hallway 
"""

class doubleDoors(Entrance, Item):
    name = 'double doors'
    destination = 'bridge'
    description = ('A set of double doors leading to the BRIDGE.')

class officeDoor(Entrance, Item):
    name = 'office door'
    destination = 'HAOoBaM'
    description = ('A door to a side office.')

class stairsDown(Entrance, Item):
    name = 'stairs down'
    destination = 'stairwell'
    description = ('A set of stairs going back down.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


upperHall = {
    'description': ('You are in the UPPER HALLWAY.'),
    'items': [
        
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': doubleDoors(),
        'workwards': officeDoor(),
        'down': stairsDown(),
    }
}
