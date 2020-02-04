from items.item import Item
from items.mixins import Entrance

""" The Zen Garden
"""

class RecRoomDoor(Entrance, Item):
    name = 'a door'
    entrance_destination = 'recRoom'
    description = ('A chrome door.')

class toEscapePods(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'escapePods'
    description = ('A sturdy chrome ladder.')

zen_garden = {
    'description': (''),
    'items': [],
    'people': [],
    'exits': {
        'north': RecRoomDoor(),
        'down': toEscapePods(),
    }
}
