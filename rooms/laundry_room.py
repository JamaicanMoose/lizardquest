from items.item import Item
from items.mixins import Entrance

""" The Laundry Room
"""

class toDorms(Entrance, Item):
    name = 'door to dorms'
    entrance_destination = 'dorms'
    description = ('A door leading back to the DORMS.')

laundry_room = {
    'description': ('You are in the LAUNDRY ROOM'),
    'items': [],
    'people': [],
    'exits': {
        'bedwards': toDorms(),
    }
}
