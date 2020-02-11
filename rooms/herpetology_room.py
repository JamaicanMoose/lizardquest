from items.item import Item
from items.mixins import Entrance, Fixed
from errors import CommandFailed
from scenarios.scenario import Scenario
from time import sleep

class RecRoomDoor(Entrance, Item):
    name = 'door'
    entrance_destination = 'recRoom'
    description = 'A door to the rec room.'

class Fridge(Fixed, Item):
    name = 'fridge'
    alt_names = ['refridgerator', 'ice box']
    description = '''\
A tall white refridgerator.'''
    take_fail_text = '''\
You try to pick up the fridge but it\'s just too heavy to move.'''

    def open(self):
        class FridgeOpen(Scenario):
            class Lettuce(Item):
                name = 'fresh lettuce'
                prettyname = 'Fresh Lettuce'
                alt_names = ['lettuce']
                description = '''\
Some perfectly fresh lettuce.
A lizard would have probably loved to eat it.'''

            def start(self, _state = None):
                def _n():
                    for item in _game_state['player'].state['inventory']:
                        if 'lettuce' in item.name:
                            print('You already have some lettuce, leave some for the lizards.')
                            return

                    print('Would you like to take some?')
                    choices = []
                    choices.append(('Yes, give me some of that yummy green stuff', _a,))
                    choices.append(('No, who likes lettuce', lambda: None,))
                    Scenario.choose(choices)

                def _a():
                    print('You take some lettuce.')
                    _game_state['player'].state['inventory'].append(self.Lettuce())
                    pass

                _n()

        print('You open the fridge and inside is a mountain of lettuce!')
        sleep(1)
        FridgeOpen().start()
        sleep(1)
        print('You close the fridge.')

    def close(self):
        print('The fridge is already closed, that\'s how it keeps things cold.')
        raise CommandFailed()

herpetology_room = {
    'description': ('You are in the HERPETOLOGY LAB'),
    'items': [
        Fridge()
    ],
    'people': [],
    'exits': {
        'north': RecRoomDoor(),
    }
}
