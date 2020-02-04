from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Escpae Pod Storage Room
"""

class toZenGarden(Entrance, Item):
    name = 'ladder'
    destination = 'zenGarden'
    description = ('A sturdy chrome ladder.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


escapePods = {
    'description': ('you are in the Escape Pod Hanger.'),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': toZenGarden(),
    }
}
