from items.item import Item
from items.mixins import Entrance, Fixed, Readable
from person import Person
from scenarios.scenario import Scenario
from time import sleep

""" The Captain's Room
"""

class toBridge(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'bridge'
    description = ('A sturdy chrome ladder, leading back up to the BRIDGE.')

_captains_log_desc = '''\
A dusty old journal sitting on the desk. It\'s got a bookmark stuck about
halfway through the volume.'''

_captains_log_text = '''\
Stardate 97664.16:

I wish I knew how to get the butler to catch onto my hints...I've been
dropping them all day! Does he think that anyone actually requests this many
sandwiches?

Stardate 97683.32:

Saw a cool star today. Not the usual one, this is the other one.

Stardate 97714.42:

We picked up a passenger about a week ago, though they\'ve been out cold
since then. Hopefully they don\'t react too poorly to being brought onboard
our ol' ship of friends. Better than the last guy, anyways, we had to drop him
off at the nearest port after he threatened to open the door to Room.'''

class captainsLog(Fixed, Readable, Item):
    name = 'captain\'s log'
    alt_names = ['log', 'journal', 'notebook']
    pronouns = ('she', 'her', 'her', 'hers', 'herself')
    description = _captains_log_desc
    text = _captains_log_text
    take_fail_text = '''\
It\'s probably unwise to take the captain\'s log while she\'s watching!'''

class captainConvo(Scenario):

    def start(self, state):
        pass

        # accolade/title for giving sandwich
        _game_state['player'].add_accolade('')

_captain_desc = '''\
The captain of the ship, easily identifiable by her magnificent
captain\'s hat.'''

class captain(Person):
    name = 'captain'
    alt_names = ['pirate captain', 'space pirate captain', 
                 'roberto', 'captain roberto']
    description = _captain_desc
    scenario = captainConvo()

captains_room = {
    'description': ('You are in the Captain\'s Room.'),
    'items': [],
    'people': [captain()],
    'exits': {
        'north': toBridge(),
    }
}
