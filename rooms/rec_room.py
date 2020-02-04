from items.item import Item
from items.mixins import Entrance

""" RecRoom
"""

class toBrig(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'brig'
    description = 'A ladder to the ship\'s BRIG.'

class toHerpetology(Entrance, Item):
    name = 'door to herpetology room'
    entrance_destination = 'herpetologyRoom'
    description = 'A door to the ship\'s HERPETOLOGY LAB.'

class toDorms(Entrance, Item):
    name = 'door to dorms'
    entrance_destination = 'dorms'
    description = 'A door to the ship\'s DORM annex.'

class toZen(Entrance, Item):
    name = 'door to zen garden'
    entrance_destination = 'zenGarden'
    description = 'A door to the ship\'s ZEN GARDEN.'

class toStairwell(Entrance, Item):
    name = 'stairs'
    entrance_destination = 'stairwell'
    description = 'A STAIRCASE leading upwards.'

class toKitchen(Entrance, Item):
    name = 'kitchen'
    entrance_destination = 'kitchen'
    description = 'A door to the ship\'s KITCHEN.'

rec_room = {
    'description': 'You are in the REC ROOM.',
    'items': [],
    'people': [],
    'exits': {
        'down': toBrig(),
        'up': toStairwell(),
        'lizardwards': toHerpetology(),
        'foodwards': toKitchen(),
        'bedwards': toDorms(),
        'zenwards': toZen(),
    }
}
