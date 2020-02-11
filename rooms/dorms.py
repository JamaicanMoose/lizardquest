from items.item import Item
from items.mixins import Entrance, Openable, Fixed

""" The Dorms
"""

class RecRoomDoor(Entrance, Item):
    name = 'rec room door'
    entrance_destination = 'recRoom'
    description = ('A large, circular door leading back to the REC ROOM.')

class toLaundryRoom(Entrance, Item):
    name = 'laundry room door'
    entrance_destination = 'laundryRoom'
    description = ('A small door, leading into the LAUNDRY ROOM.')

class cardTable(Fixed, Item):
    name = 'card table'
    alt_names=['tabel','card tabel','table']
    description = '''\
    A card table, with cards strewn all about the floor.
    It seems as though the pirates were engaged in a game of full-contact Go Fish.
'''
    take_fail_text = '''\
You can't!
The table would create a DEADLY TOXIN if placed in your inventory!

...nah, I'm just kidding.
But you don't need it, and it's heavy, so you leave it where it is.'''
    

class flair(Fixed, Item):
    name = 'flair'
    alt_names=['posters','decorations','pin-ups','photos','photographs','lizards']
    description = '''\
The walls are covered floor to ceiling in all sorts of memoribilia.
It's Honestly somewhat impressive - it puts together a nice picture of the folks that live here.
You get the sense that people around here really care about each other.
Some highlights:
- A bunch of photos of the same group, smiling and celebrating.
  The photos in the series are taken from further and further away.
  Viewed as a whole, it becomes clear that the photos were taken as the photographer attempted to steal the phone.
- Scribbly crayon art, labelled \"By Jeffy, Age 6.\".
  A note is attached to it, asking people at \"Mom\'s work\" to write \"fam-nail\".
  Several post-it notes surround the piece, all with encouraging messages.
- A dedicated wall of lizard-themed pin-ups, featuring models of all body types, genders, and species.
  Everyone knows what lizard-themed pin-ups look like, so I won\'t waste any more time describing them.
  These are some pretty nice ones, but they don't hold a candle to your colleciton.
'''
    take_fail_text = '''\
You already own all the lizard pin-ups you need.
Besides, this stuff seems mostly sentimental.'''

class breadBox(Openable, Fixed, Item):
    name = 'breadbox'
    alt_names = ['bread box', 'box','bread zone','shelf','shelves','bookcase','breadcase']
    description = '''\
A hand-crafted breadbox with a clear lid. Inside, you can see several loaves, placed with care.
The box is pleasantly warm to the touch - it appears to be heated, to keep the bread fresh.
...Thinking about it, you're actually unsure if \'breadbox\' is the most accurate name for this thing.
It's about the size of a small bookcase.

... That said, it's a box. And it has bread. So... breadbox it is.
'''
    take_fail_text = '''\
You try to pick up the breadbox, but it appears to be bolted to the wall.'''

    def open(self):
        class BoxOpen(Scenario):
            class bread(Item):
                name = 'bread'
                prettyname = 'Homemade Bread'
                alt_names = ['Bread', 'food']
                description = '''\
A fragrant, warm loaf of fresh bread.
Whoever made this has a real talent for baking.'''

            def start(self, _state = None):
                def _n():
                    for item in _game_state['player'].state['inventory']:
                        if 'bread' in item.name:
                            print('Your enthusiasm for bread is admirable, but you should use what you have before grabbing more.')
                            return

                    print('Would you like to take a loaf?')
                    choices = []
                    choices.append(('Yes, of course! I\'m sure they won\'t mind.', _a,))
                    choices.append(('No! I\'m no thief!', lambda: None,))
                    Scenario.choose(choices)

                def _a():
                    print('You take a fresh loaf of BREAD.')
                    _game_state['player'].state['inventory'].append(self.bread())
                    pass

                _n()

        print('You open the breadbox, your eyes falling on row after row of beautiful loaves of bread.')
        sleep(1)
        BoxOpen().start()
        sleep(1)
        print('You close the breadbox, your curiosity sated.')

    def close(self):
        print('The breadbox is already closed! That was very considerate of you, though.')
        if not _game_state['player'].has_accolade('the Conscientious'):
            _game_state['player'].add_accolade('the Conscientious')
        raise CommandFailed()

dorms = {
    'description': ('You find yourself in the common room of a set of DORMS.\n'+
                    'The common room itself is semi-circular, and doors leading to individual rooms\n'+
                    'extend from its walls like spokes on the bifurcated wheel of a severely damaged bicyle.\n'+
                    'What little wallspace remains between the tightly-packed doors is covered\nin bits'+
                    'of FLAIR - posters, photographs, lizard-themed pin-ups and the like.\n'+
                    'As for furniture, there isn\'t much.\nThere is a CARD TABLE in the middle of the room, flanked by chairs.\n'+
                    'Other than that, the only piece of furniture is a large, wooden BREADBOX.\n'+
                    'You don\'t really want to sneak into people\'s rooms... That\'s their personal space.\n'+
                    'Ignoring those, there are only two doors worth further investigation-- the REC ROOM DOOR and the LAUNDRY ROOM DOOR.'),
    'items': [breadBox(),
              flair(),
              cardTable()],
    'people': [],
    'exits': {
        'hubwards': RecRoomDoor(),
        'laundrywards': toLaundryRoom(),
    }
}
