from items.item import Item
from items.mixins import Entrance

""" The Stairwell
"""

class downToRecRoom(Entrance, Item):
    name = 'downstairs'
    entrance_destination = 'recRoom'
    description = ('A set of stairs leading down to the RECREATION ROOM.')

class upToUpperHall(Entrance, Item):
    name = 'upstairs'
    entrance_destination = 'upperHall'
    description = ('A set of stairs leading up to the UPPER HALLWAY.')

stairwell = {
    'description': ('You are on the landing of the grand stairwell.'),
    'items': [],
    'people': [],
    'exits': {
        'down': downToRecRoom(),
        'up': upToUpperHall(),
    }
}
