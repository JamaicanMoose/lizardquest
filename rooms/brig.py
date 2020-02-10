from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed
from person import Person
from scenarios.scenario import Scenario

""" The Brig
"""

_ladder_description = '''\
A sturdy chrome ladder.
Presumably this leads to an upper floor of the ship.

A small label next to the ladder reads:
\"To Rec Room\"'''

class Ladder(Entrance, Item):
    name = 'chrome ladder'
    alt_names = ('ladder',)
    entrance_destination = 'recRoom'
    description = _ladder_description

_grid_of_photos_description = '''\
As you get closer you realize that every photo in the grid depicts
the same person.
Sixty pictures of Guard stare back at you, each one prouder and more
enthusiastic than the last.
Beneath each is a simple metal plaque:
\"Employee of the Month\"'''

class EmployeeBoard(Fixed, Item):
    name = 'grid of photos'
    alt_names = ['photos']
    description = _grid_of_photos_description
    prettyname = 'A Grid Of Photos'

    def examine(self):
        self.alt_names.append('grid of photos')
        self.name = 'meaningless awards'
        self.prettyname = self.name.title()
        self.alt_names.append('awards')
        _game_state['_brig_employee_board_examined'] = True
        Item.examine(self)


_medal_front_text = '''\
\"The Department of Bureaucracy and Mail recognizes the recipient of this
medal as a Good and Special Boy\"
On the back, the words \"You Performed Adequately!\" are printed in Comic Sans
followed by a ridiculous amount of fine print.'''
_medal_back_text = '''\
\"You Performed Adequately!\"'''
_medal_description = f'''\
A gold star, polised to a mirror sheen.'''
_medal_take_fail_text = '''\
He doesn\'t look willing to give it to you, and given how focused he is,
it doesn\'t seem like taking it is an option.'''

class Medal(Fixed, Readable, Item):
    name = 'medal'
    alt_names = ('award',)
    text = _medal_front_text
    description = _medal_description
    take_fail_text = _medal_take_fail_text

class Flask(Fixed, Item):
    name = 'ye flask'
    alt_names = ['flask']
    take_fail_text = '''\
You can\'t get ye flask.

You sit imagining why on Earth you can\'t get ye flask.
You give up because the game\'s certainly not going to tell you.'''

class GuardConversation(Scenario):

    state = {}

    def start(self, guard):

        def guard_say(text):
            name = 'BEN THE GUARD' if 'ben' in guard.alt_names else 'GUARD'
            print(f'{name} : \"', end='')
            print(text, end='')
            print(f'\"')

        def anything_else():
            guard_say('''\
Was there anything else you wanted to talk about?'''
            )

        def _n():
            choices = []
            choices.append(('Your medal', _a,))
            if 'ben' not in guard.alt_names:
                choices.append(('Your name', _c,))
            if '_brig_employee_board_examined' in _game_state:
                choices.append(('Employee of the month', _b,))
            choices.append(('Nothing', _end,))
            Scenario.choose(choices)

        def _a():
            guard_say('''\
Ahh you\'ve spied my medal!
The cap\'n gave it to me after I captured my 10th prisoner.'''
            )
            choices = []
            choices.append(('Why so many prisoners?', _aa,))
            choices.append(('Can I have it?', _ab,))
            choices.append(('*Leave*', lambda: _end(rude=True),))
            Scenario.choose(choices)

        def _b():
            print('The guards smiles.')
            guard_say('''\
Yep, recognition for my hard work.
No one else even stood a chance.'''
            )
            anything_else()
            _n()

        def _c():
            guard_say('''\
Oh my name? Its Benjamin, though most people just call me Ben.'''
            )
            guard.alt_names.append('ben')
            guard.alt_names.append('benjamin')
            anything_else()
            _n()

        def _aa():
            guard_say('''\
The cap\'n says that we\'ve gotta keep up appearances.
You\'re more than free to go though.
Somma the ones before you left and somma them stayed.'''
            )
            _game_state['player'].add_accolade('The Captured but Free')
            anything_else()
            _n()

        def _ab():
            guard_say('''\
Why should I give it to you?
Does it have your name on it?'''
            )
            print('''
The guard clutches his medal tightly.'''
            )
            choices = []
            choices.append(('Yes', _aba,))
            choices.append(('No', _abb,))
            Scenario.choose(choices)

        def _aba():
            pname = _game_state['player']._prettyname.lower()
            if pname == 'ben' or pname == 'benjamin':
                guard_say('''\
Huh.
I guess it is.
But it was given to me so i\'m not giving it up.'''
                )
                anything_else()
                _n()
            else:
                guard_say('''\
You\'re lying.
And I don\'t like talking to liars.'''
                )
                _game_state['player'].add_accolade('Big Fat Liar')

        def _abb():
            guard_say('''\
Then you shouldn\'t be asking for it.'''
            )
            anything_else()
            _n()

        def _end(rude = False):
            if rude:
                guard_say('''\
Well I guess we can be done talking.'''
                )
                _game_state['player'].add_accolade('Rude Talker')
            else:
                guard_say('''\
Oh ok.
I was so excited to have a new friend on the ship but I guess we can talk
another time.'''
                )
            print('''\
The guard goes back to polishing his medal.'''
            )

        if _game_state['player'].has_accolade('Big Fat Liar'):
            guard_say('''\
I don\'t talk to liars.'''
            )
            return

        guard_say('''\
Hi! What did you want to talk about?'''
        )
        _n()

_guard_description = f'''\
He\'s wearing a black uniform and is clutching what looks to be a medal of
some kind.'''

class Guard(Person):
    name = 'guard'
    scenario = GuardConversation()
    description = _guard_description
    alt_names = []

_brig_description = '''\
Vacant cells line either side of the central hall.
On the other end of the hall, there is a GRID OF PHOTOS.
A GUARD sits in the middle of the hall, proudly polishing a MEDAL of
some fashion.'''

brig = {
    'description': (_brig_description),
    'items': [
        EmployeeBoard(),
        Medal(),
        Flask()
    ],
    'people': [
        Guard()
    ],
    'exits': {
        'north': Ladder(),
    }
 }
