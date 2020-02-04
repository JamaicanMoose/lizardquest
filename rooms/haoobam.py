from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" Head administrative office of bureaucracy and mail
"""

class toUpperHall(Entrance, Item):
    name = 'doors'
    destination = 'upperHall'
    description = ('Doors leading to the UPPER HALLWAY.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')


haoobam = {
    'description': ('You are in the Head Administrative Office of Bureaucracy and Mail'),
    'items': [
       
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': toUpperHall(),
    }
}
