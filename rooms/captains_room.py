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
halfway through the volume. On the cover, it reads: "Captain's Log."'''

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
    description = _captains_log_desc
    text = _captains_log_text
    take_fail_text = '''\
It\'s probably unwise to take the captain\'s log while she\'s watching!'''

class captainConvo(Scenario):

    def has_sandwich(self):
        for item in _game_state['player'].state['inventory']:
            if 'sandwich' in item.name:
                return True
        return False

    def captain_intro(self, state):
        print("The captain begins to speak as she notices you.")
        print('''\
"Hey, you. You're finally awake. You were trying to cross..."\n''')
        sleep(1)
        print("The captain catches herself mid-sentence.")
        print('''\
"...sorry, wrong prisoner. Well, I see that yer awake now, and ya've
found yer way outta the brig! I commend ye. So, how do ya like our
quaint lil' spacecraft?"''')

        choice = Scenario.pick(["It's quite nice", "Needs more lizards"])
        if choice == 0:
            print('''\
"Glad ya think so! I've put a lotta care into 'er over the years, so it's
nice to hear that she shows it!"''')
        else:
            print('''\
"Ya've got that right! Ain't no such thing as a lizard-powered ship
with too many of the wriggly buggers. Specially since the lizard recession,
we've needed all we can get our hands on!''')
            sleep(1)
            print('''\
...plus, I've got a soft spot for the lil' guys. They're right cute!"''')
        sleep(1)

        _game_state['_captain_intro'] = True

    def start(self, state):
        if '_captain_intro' not in _game_state:
            self.captain_intro(state)

        if _game_state['player'].has_accolade('The Generous'):
            print('''\
"Hey, thanks again fer that sandwich!" says the captain, as she scarfs
down a bite. "Now I can focus on piloting this ship again!"''')
            return

        print('''\
"Hey, between you and me, if ya happen to find a sandwich on yer hands, I'd 
be happy ta relieve ya of it! I've been awful hungry, and I'm not sure where
that butler's been off to!"''')

        if not self.has_sandwich():
            return

        print("Give the captain your sandwich?")
        choice = Scenario.pick(["Sure, sharing is caring", "No way"])
        if choice == 0:
            print('''
"Really?" says the captain, "Ya'd give me that delicious lookin' sandwich,
after we only just met? Well thank you very much!"''')
            sleep(1)
            print("You hand the captain your sandwich.")
            
            for item in _game_state['player'].state['inventory']:
                if 'sandwich' in item.name:
                    _game_state['player'].state['inventory'].remove(item)

            sleep(1)
            print('''\
"Consider yerself welcome aboard our ship, stay as long as ye'd like!"''')
        else:
            return

        # accolade/title for giving sandwich
        _game_state['player'].add_accolade('The Generous')

_captain_desc = '''\
The captain of the ship, easily identifiable by her magnificent
captain\'s hat.'''

class captain(Person):
    name = 'captain'
    alt_names = ['pirate captain', 'space pirate captain', 
                 'roberto', 'captain roberto']
    pronouns = ('she', 'her', 'her', 'hers', 'herself')
    description = _captain_desc
    scenario = captainConvo()

_captains_room_desc = '''\
You find yourself in the CAPTAIN'S ROOM. You see some furniture, including a
desk with a JOURNAL on it. The CAPTAIN is sitting at her chair by the desk,
wearing her captain's hat proudly.'''

captains_room = {
    'description': _captains_room_desc,
    'items': [captainsLog()],
    'people': [captain()],
    'exits': {
        'north': toBridge(),
    }
}
