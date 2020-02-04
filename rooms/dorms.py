from items.item import Item
from items.mixins import Entrance

""" The Dorms
"""

class RecRoomDoor(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'recRoom'
    description = ('A sturdy chrome ladder.')

class toLaundryRoom(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'laundryRoom'
    description = ('A sturdy chrome ladder.')

dorms = {
    'description': ('A set of dorms.'),
    'items': [],
    'people': [],
    'exits': {
        'north': RecRoomDoor(),
        'in': toLaundryRoom(),
    }
}
