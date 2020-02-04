from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Stairwell 
"""

class downToRecRoom(Entrance, Item):
    name = 'downstairs'
    destination = 'recRoom'
    description = ('A set of stairs leading down to the RECREATION ROOM.')

class upToUpperHall(Entrance, Item):
    name = 'upstairs'
    destination = 'upperHall'
    description = ('A set of stairs leading up to the UPPER HALLWAY.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


stairwell = {
    'description': ('You are on the landing of the grand stairwell.'),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'down': downToRecRoom(),
        'up':upToUpperHall(),
    }
}
