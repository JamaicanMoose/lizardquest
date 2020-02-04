from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Captain's Room [Room (0,0,0)]
"""

class toBridge(Entrance, Item):
    name = 'ladder'
    destination = 'bridge'
    description = ('A sturdy chrome ladder.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


captainsRoom = {
    'description': ('You are in the Captain\'s Room.'),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': toBridge(),
    }
}
