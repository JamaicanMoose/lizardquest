from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Herpetology Room [Room (0,0,0)]
"""

class toUpperHall(Entrance, Item):
    name = 'door'
    destination = 'upperHall'
    description = ('A large set of double doors.')

class toCaptainsRoom(Entrance, Item):
    name = 'ladder'
    destination = 'captainsRoom'
    description = ('A sturdy chrome ladder.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


bridge = {
    'description': (''),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': toUpperHall(),
        'down':toCaptainsRoom(),
    }
}
