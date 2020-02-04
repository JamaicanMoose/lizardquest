from items.item import Item
from items.mixins import Entrance, Openable, Readable
from person import Person

""" The Hollow [Room (0,0,0)]
"""

class Opening(Entrance, Item):
    name = 'opening'
    entrance_destination = (1,0,0)
    description = 'A door made from a large piece of leather'

class Grate(Entrance, Openable, Item):
    name = 'grate'
    open = False
    entrance_destination = (0,0,-1)

    @property
    def description(self):
        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')

class Plea(Readable, Item):
    name = 'plea for help'
    text = 'Requestor: Baroq, Town Sherrif\nRequest: Investigate the source of the earthquakes in the Evergreen Forest and eliminate if possible.\nThreat Level: [3]'
    description = 'A folded note, it has multiple pin holes in it from where it was fixed to a board.'

room_0_0_0 = {
    'description': 'The chamber is relatively bare except for small metal tubes that crisscross the ceiling.',
    'items': [
        Plea()
    ],
    'people': [
        Person()
    ],
    'exits': {
        'north': Opening(),
        'south': Grate(),
    }
}
