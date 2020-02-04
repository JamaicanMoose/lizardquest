from items.item import Item
from items.mixins import Entrance

""" The Escpae Pod Storage Room
"""

class toZenGarden(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'zenGarden'
    description = ('A sturdy chrome ladder.')

escape_pods = {
    'description': ('you are in the Escape Pod Hanger.'),
    'items': [],
    'people': [],
    'exits': {
        'north': toZenGarden(),
    }
}
