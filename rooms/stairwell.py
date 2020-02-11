from items.item import Item
from items.mixins import Entrance, Readable

""" The Stairwell
"""

class memo(Readable, Item):
    name = 'note'
    alt_names = ['memo', 'paper']
    description = ('A small piece of paper labelled \"MEMO.\"')
    text = ('MEMO.\n'
            'To whom it may concern: it has recently been brought to my '
            'attention that our fish, Comet, Pretzel, and Sheryl, can speak, '
            'and possess unbounded wisdom.\nThis manner should probably be '
            'looked into when someone finds the motivation to do so.')

    def examine(self):
        Item.examine(self)

class downToRecRoom(Entrance, Item):
    name = 'downstairs'
    entrance_destination = 'recRoom'
    description = ('A set of stairs leading down to the RECREATION ROOM.')

class upToUpperHall(Entrance, Item):
    name = 'upstairs'
    entrance_destination = 'upperHall'
    description = ('A set of stairs leading up to the UPPER HALLWAY.')

stairwell = {
    'description': ('You are on the landing of the grand stairwell.\n'
                    'Its pristine marbled floors amaze you, a stark '
                    'contrast to the chrome that defines the rest of the '
                    'ship\'s interior.\nSurely a bold design decision by '
                    'an astute interior designer.\n'
                    'You also notice a NOTE that has fallen on the floor.'),
    'items': [memo()],
    'people': [],
    'exits': {
        'down': downToRecRoom(),
        'up': upToUpperHall(),
    }
}
