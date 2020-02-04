from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Zen Garden
"""

class RecRoomDoor(Entrance, Item):
    name = 'a door'
    destination = 'recRoom'
    description = ('A chrome door.')

class toEscapePods(Entrance, Item):
    name = 'ladder'
    destination = 'escapePods'
    description = ('A sturdy chrome ladder.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


zenGarden = {
    'description': (''),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': RecRoomDoor(),
        'down': toEscapePods(),
    }
}
