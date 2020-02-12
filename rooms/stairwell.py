from items.item import Item
from items.mixins import Entrance, Readable

""" The Stairwell
"""

class Memo(Readable, Item):
    name = 'note'
    alt_names = ['memo', 'paper']
    description = 'A small piece of paper labelled \"MEMO.\"'
    text = '''\
MEMO.
To whom it may concern: it has recently been brought to my attention that our
fish, Comet, Pretzel, and Sheryl, can speak, and possess unbounded wisdom.
This manner should probably be looked into when someone finds the motivation to do so.'''


class StaircaseToRecRoom(Entrance, Item):
    name = 'staircase'
    alt_names = ['down', 'grand staircase', 'stairs']
    entrance_destination = 'recRoom'
    entrance_destination_name = 'rec room'
    entrance_type = 'staircase'
    description = '''\
A grand staircase that lead downwards.

At your feet is a small label.'''


class StaircaseToUpperHall(Entrance, Item):
    name = 'staircase'
    alt_names = ['up', 'grand staircase', 'stairs']
    entrance_destination = 'upperHall'
    entrance_destination_name = 'upper hall'
    entrance_type = 'staircase'
    description = '''\
A grand staircase that lead upwards.

At your feet is a small label.'''


stairwell = {
    'description': '''\
You are on the landing of the grand stairwell.
Its pristine marbled floors amaze you, a stark contrast to the chrome that defines the rest of the ship\'s interior.
Surely a bold design decision by an astute interior designer.''',
    'items': [
        Memo()
    ],
    'people': [],
    'exits': {
        'down': StaircaseToRecRoom(),
        'up': StaircaseToUpperHall(),
    }
}
