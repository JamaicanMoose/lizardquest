from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Dorms
"""

class RecRoomDoor(Entrance, Item):
    name = 'ladder'
    destination = 'recRoom'
    description = ('A sturdy chrome ladder.')

class toLaundryRoom(Entrance, Item):
    name = 'ladder'
    destination = 'laundryRoom'
    description = ('A sturdy chrome ladder.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


dorms = {
    'description': ('A set of dorms.'),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': RecRoomDoor(),
        'in': toLaundryRoom(),
    }
}
