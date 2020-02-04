from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Laundry Room 
"""

class toDorms(Entrance, Item):
    name = 'door to dorms'
    destination = 'dorms'
    description = ('A door leading back to the DORMS.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


laundryRoom = {
    'description': ('You are in the LAUNDRY ROOM'),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'bedwards': toDorms(),
    }
}
