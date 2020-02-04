from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Kitchen
"""

class RecRoomDoor(Entrance, Item):
    name = 'rec room'
    destination = 'recRoom'
    description = ('A door to the RECREATION ROOM.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


kitchen = {
    'description': ('You are in the kitchen.'),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': RecRoomDoor(),
    }
}
