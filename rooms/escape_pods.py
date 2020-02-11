from items.item import Item
from items.mixins import Entrance, Readable, Fixed
from time import sleep
from util import endgame

""" The Escpae Pod Storage Room
"""

class toZenGarden(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'zenGarden'
    description = ('A sturdy chrome ladder.')

class EscapePod(Readable, Fixed, Item):
    @property
    def prettyname(self):
        return self.name.title()

    description = '''\
A small one person escape pod.
Inside the escape pod are a small recepticle labeled \"LIZARD\" and a large
red button that reads \"LAUNCH\".
It has a label on it.
'''
    def __init__(self, num, destination):
        self.name = f'escape pod {num}'
        self._escape_pod_destination = destination
        self.text = f'Escape Pod to {destination.title()}'

    def use(self):
        pinv = _game_state['player'].state['inventory']
        for item in pinv:
            if item.name.endswith('lizard'):
                lizard = item
                print(f'''\
You get into the escape pod and insert the {lizard.name} into the \"LIZARD\"
recepticle.
The {lizard.name} gets sucked out of view.'''
                )
                sleep(5)
                print(f'''\
The escape pod shakes and you watch out the back window as the ship fades away.'''
                )
                sleep(1)
                print('.')
                sleep(1)
                print('.')
                sleep(1)
                print('.')
                sleep(1)
                print(f'''\
Presumably you are being taken to {self._escape_pod_destination} but who knows.'''
                )
                if _game_state['player'].has_accolade('The Hungry'):
                    sleep(1)
                    print('''\
As you fly away you feel like you\'ve forgotten something.
A rumbling in your stomach lets you know that you never did manage to
get the sandwich that you had been longing for all this time.'''
                    )
                elif _game_state['player'].has_accolade('The Lonely'):
                    sleep(1)
                    print('''\
As you fly away you feel like you\'ve forgotten something.
A rumbling in your stomach lets you know that you never did manage to
get the sandwich that you had been longing for all this time.'''
                    )
                sleep(2)
                endgame()
        print('''\
You get into the escape pod and press the \"LAUNCH\" button.
'''
        )
        sleep(3)
        print('''\
A message appears on the console: \"Lizard Recepticle Empty. Launch Has Been Cancelled.\"
Nothing else seems to be happening, so you get out of the escape pod.
'''
        )

escape_pods = {
    'description': ('You are in the Escape Pod Hangar.\n'+
                    'Despite the size of the ship, it appears that there are only three emergency escape pods.\n'+
                    'Each of them has a small screen displaying a number, as well as a pre-programmed location:\n'+
                    'ESCAPE POD 1, ESCAPE POD 2, and ESCAPE POD 3.\nThe locations are written in smaller text, and would require a closer look.\n'+
                    'The room is pretty empty, otherwise -- It\'s a Space OSHA violation to have any trip hazards near emergency equipment.\n'+
                    'Behind you is a LADDER that goes back to the ZEN GARDEN.\n'),
    'items': [
        EscapePod(1, 'Safe Planet'),
        EscapePod(2, 'A Wormhole'),
        EscapePod(3, 'A Real Pirate Ship')
    ],
    'people': [],
    'exits': {
        'zenwards': toZenGarden(),
    }
}
