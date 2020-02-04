from items.item import Item
from items.mixins import Entrance

""" Hub [Room (1,0,0)]
"""

class toBrig(Entrance, Item):
    name = 'ladder'
    destination = 'brig'
    description = 'A ladder to the ship\'s BRIG.'

class toHerpetology(Entrance, Item):
    name = 'door to herpetology room'
    destination = 'herpetologyRoom'
    description = 'A door to the ship\'s HERPETOLOGY LAB.'

class toDorms(Entrance, Item):
    name = 'door to dorms'
    destination = 'dorms'
    description = 'A door to the ship\'s DORM annex.'

class toZen(Entrance, Item):
    name = 'door to zen garden'
    destination = 'zenGarden'
    description = 'A door to the ship\'s ZEN GARDEN.'

class toStairwell(Entrance, Item):
    name = 'stairs'
    destination = 'stairwell'
    description = 'A STAIRCASE leading upwards.'

class toKitchen(Entrance, Item):
    name = 'kitchen'
    destination = 'kitchen'
    description = 'A door to the ship\'s KITCHEN.'

room_1_0_0 = {
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
