from items.item import Item
from items.mixins import Entrance

""" Head administrative office of bureaucracy and mail
"""

class toUpperHall(Entrance, Item):
    name = 'doors'
    entrance_destination = 'upperHall'
    description = ('Doors leading to the UPPER HALLWAY.')

haoobam = {
    'description': ('You are in the Head Administrative Office of Bureaucracy and Mail'),
    'items': [],
    'people': [],
    'exits': {
        'north': toUpperHall(),
    }
}
