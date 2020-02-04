from items.item import Item
from items.mixins import Entrance

""" The Herpetology Room [Room (0,0,0)]
"""

class toUpperHall(Entrance, Item):
    name = 'door'
    entrance_destination = 'upperHall'
    description = ('A large set of double doors.')

class toCaptainsRoom(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'captainsRoom'
    description = ('A sturdy chrome ladder.')

bridge = {
    'description': (''),
    'items': [],
    'people': [],
    'exits': {
        'north': toUpperHall(),
        'down': toCaptainsRoom(),
    }
}
