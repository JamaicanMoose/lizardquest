from items.item import Item
from items.mixins import Entrance

""" The Herpetology Room
"""

class RecRoomDoor(Entrance, Item):
    name = 'door'
    entrance_destination = 'recRoom'
    description = ('A door to the REC ROOM.')

herpetology_room = {
    'description': ('You are in the HERPETOLOGY LAB'),
    'items': [],
    'people': [],
    'exits': {
        'north': RecRoomDoor(),
    }
}
