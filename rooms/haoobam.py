from items.item import Item
from items.mixins import Entrance, Readable, Fixed, Breakable
from scenarios.scenario import Scenario

""" Head administrative office of bureaucracy and mail
"""

class toUpperHall(Entrance, Item):
    name = 'double door'
    entrance_destination = 'upperHall'
    description = 'Doors leading to the upper hallway.'

class Desk(Fixed, Item):
    name = 'desk'
    description = '''\
A rectangular desk that seems to be made of plywood.
It is probably the most boring desk you\'ve ever seen.'''
    take_fail_text = '''\
You try to grab the desk and take it with you but it seems to be fixed
to the floor.
'''

class LabelMaker(Breakable, Readable, Item):
    name = 'label maker'
    text = 'Label Maker'
    _label_maker_num_labels = 1

    @property
    def description(self):
        labelstr = 'It seems to have one label left in it.' if self._label_maker_num_labels else 'Its empty.'
        return f'''\
A label maker, it makes labels.
{labelstr}
And it has a label on it... how recursive.'''

    def use(self):
        class LabelMakerUse(Scenario):
            def start(self, labelmaker):
                def _n():
                    print('There are three phrases keyed into the printer.')
                    print('What would you like to print?')
                    choices = []
                    choices.append(('Printer Of Labels', _lbp,))
                    choices.append(('Cares About Others', _a,))
                    choices.append(('Iron Chef', _b,))
                    choices.append(('Lizard Archwizard', _c,))
                    choices.append(('* Leave *', _d,))
                    Scenario.choose(choices)

                def _lbp():
                    print('You stick the label on yourself.')
                    labelmaker._label_maker_num_labels -= 1
                    _game_state['player'].add_accolade('Printer Of Labels')

                def _a():
                    print('You stick the label on yourself.')
                    labelmaker._label_maker_num_labels -= 1
                    _game_state['player'].add_accolade('Cares About Others')

                def _b():
                    print('You stick the label on yourself.')
                    labelmaker._label_maker_num_labels -= 1
                    _game_state['player'].add_title('Iron Chef')

                def _c():
                    print('You stick the label on yourself.')
                    labelmaker._label_maker_num_labels -= 1
                    _game_state['player'].add_title('Lizard Archwizard')

                def _d():
                    print('You don\'t print anything and leave it for someone else.')

                _n()

        if self._label_maker_num_labels:
            LabelMakerUse().start(self)
        else:
            print('It seems like there aren\'t any labels left.')


haoobam = {
    'description': '''\
A really bland office with cream colored walls and a single desk.''',
    'items': [
        Desk(),
        LabelMaker()
    ],
    'people': [],
    'exits': {
        'north': toUpperHall(),
    }
}
