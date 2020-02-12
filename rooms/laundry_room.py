from items.item import Item
from items.mixins import Entrance
from scenarios.scenario import Scenario
from time import sleep
from person import Person

""" The Laundry Room
"""

class toDorms(Entrance, Item):
    name = 'door to dorms'
    entrance_destination = 'dorms'
    description = ('A door leading back to the DORMS.')

class foldedClothes(Item):
    name = 'clothes'
    alt_names = ['laundry', 'folded clothes']
    description = 'A nicely folded set of space pirate clothes.'

    @property
    def can_take(self):
        _game_state['player'].add_title('Fashion Criminal')
        return True

    def use(self):
        sleep(2)
        print("You put on the stolen space pirate outfit. Stylish!")
        return

class crossword(Scenario):

    def start(self, state):
        print('You try to get the space pirate\'s attention.')
        sleep(1)
        print("After a moment, they look up at you.")

        if '_puzzle_solved' in _game_state:
            print("\"Hey, thanks for helping me solve that puzzle!\"")
            return
        elif _game_state['player'].has_title('Fashion Criminal'):
            print("\"Go away, thief.\"")
            return

        print('''\
Gesturing at a row of tiles on his crossword puzzle, the pirate reads
the clue from the puzzle:
\"\"''')
        _game_state['player'].add_title('Puzzle Solver Extraordinaire')

_crossword_pirate_desc = '''\
A space pirate hunched over a desk, starting at, upon closer inspection,
what appears to be a CROSSWORD PUZZLE.'''

class crosswordPirate(Person):
    name = 'pirate'
    alt_names = ['space pirate']
    description = _crossword_pirate_desc
    scenario = crossword()

_laundry_room_desc = '''\
Based on the machines spinning and whirring around you, you judge that 
you are in the ship's LAUNDRY ROOM. A pile of folded CLOTHES sits on a table.
A SPACE PIRATE is focused intently on a piece of paper, pencil in hand.'''

laundry_room = {
    'description': _laundry_room_desc,
    'items': [foldedClothes()],
    'people': [crosswordPirate()],
    'exits': {
        'bedwards': toDorms(),
    }
}
