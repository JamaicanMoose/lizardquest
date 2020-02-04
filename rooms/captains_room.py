from items.item import Item
from items.mixins import Entrance

""" The Captain's Room
"""

class toBridge(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'bridge'
    description = ('A sturdy chrome ladder.')

captains_room = {
    'description': ('You are in the Captain\'s Room.'),
    'items': [],
    'people': [],
    'exits': {
        'north': toBridge(),
    }
}
