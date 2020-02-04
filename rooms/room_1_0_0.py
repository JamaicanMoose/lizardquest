from items.item import Item
from items.mixins import Entrance

""" Hallway [Room (1,0,0)]
"""

class Opening(Entrance, Item):
    name = 'opening'
    destination = (0,0,0)
    description = 'A door made from a large piece of leather'

room_1_0_0 = {
    'description': 'A coridor that looks like it was meant to be straight but the fleshlike walls add an organic quality to it.',
    'items': [],
    'people': [],
    'exits': {
        'south': Opening()
    }
}
