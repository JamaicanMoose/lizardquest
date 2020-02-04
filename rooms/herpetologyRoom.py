from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Herpetology Room 
"""

class RecRoomDoor(Entrance, Item):
    name = 'door'
    destination = 'recRoom'
    description = ('A door to the REC ROOM.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


herpetologyRoom = {
    'description': ('You are in the HERPETOLOGY LAB'),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': RecRoomDoor(),
    }
}
