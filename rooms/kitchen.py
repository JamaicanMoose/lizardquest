from items.item import Item
from items.mixins import Entrance

""" The Kitchen
"""

class RecRoomDoor(Entrance, Item):
    name = 'rec room'
    entrance_destination = 'recRoom'
    description = ('A door to the RECREATION ROOM.')

kitchen = {
    'description': ('You are in the kitchen.'),
    'items': [],
    'people': [],
    'exits': {
        'north': RecRoomDoor(),
    }
}
