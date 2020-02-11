from items.item import Item
from items.mixins import Entrance, Fixed, Readable, Openable, Lockable
from errors import CommandFailed
from scenarios.scenario import Scenario
from time import sleep
from person import Person


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


class LizardKey(Item):
    name = 'lizard key'
    description = '''\
A small metal key with teeth that look like a lizard.'''


class DarkLizard(Item):
    name = 'dark lizard'
    prettyname = 'The Dark Lizard'
    description = '''\
You look into his beady eyes and feel in your soul that in the past this
lizard has done terrible things and dabbled in dark magic that no man, or
lizard, should ever have attempted.'''
    trick_text = '''\
A small fireball appears next to the dark lizard.
It extends into a flaming hoop and it jumps through it before settling
back down.'''


class BigMouthedLizard(Item):
    name = 'big mouthed lizard'
    description = '''\
The lizard has a BIG mouth. Like seriously, you didn\'t even think lizard
mouths could get this big. Maybe its plastic surgery? Are big mouths in lizards
a thing that other lizards find appealing?'''
    trick_text = '''\
The big mouthed lizard opens its mouth even wider than it was and you see
hidden inside a full set of pearly white teeth.
Dentures or not it\'s very unsettling.'''


class SouthernTippedLizard(Item):
    name = 'southern tipped lizard'
    description = '''\
Its a lizard with a head where its butt should be and a butt where its head
should be.
You wouldn\'t expect anything less from the Lizard Wizard.'''
    trick_text = '''\
*************************************
*******************************
*****************************************

Well that\'s not something you can show on television.'''


class LizardTank(Openable, Readable, Lockable, Fixed, Item):
    lockable_locked = True
    description = '''\
It\'s a blacked out lizard tank.
It has a label on it.'''

    def __init__(self, num, lizard):
        self.num = num
        self.name = f'lizard tank {num}'
        self.alt_names = []
        self.lizard = lizard

    @property
    def text(self):
        return self.lizard.name.title()

    @property
    def prettyname(self):
        lstr = ' (Locked)' if self.lockable_locked else ''
        return f'{self.name.title()}{lstr}'

    def examine(self):
        if f'_hlab_tank{self.num}_examined' not in _game_state:
            self.alt_names.append(self.name)
            self.name = f'{self.lizard.name} tank'
            _game_state[f'_hlab_tank{self.num}_examined'] = True
        Item.examine(self)

    def unlock(self):
        for item in _game_state['player'].state['inventory']:
            if 'lizard key' in item.name:
                Lockable.unlock(self)
                print(f'Your {item.name} glows red then vanishes in a puff of smoke.')
                _game_state['player'].state['inventory'].remove(item)
                return
        print(f'You don\'t seem to have the right key for the lock.')
        raise CommandFailed()

    def open(self):
        inventory = _game_state['player'].state['inventory']
        class TankOpen(Scenario):
            def start(self, tank):
                def _n():
                    print('Would you like to....')
                    choices = []
                    choices.append(('Take the lizard', _take_lizard,))
                    for item in inventory:
                        if 'lettuce' in item.name:
                            choices.append(('Feed the lizard', _feed_lizard,))
                            break
                    choices.append(('* None *', _b,))
                    Scenario.choose(choices)

                def _take_lizard():
                    print('You pocket the lizard.')
                    inventory.append(tank.lizard)
                    sleep(.5)
                    print('''\
Almost as soon as you took the lizard the tank starts to fade from existence.'''
                    )
                    sleep(1)
                    print('.')
                    sleep(1)
                    print('.')
                    sleep(1)
                    print('.')
                    sleep(1)
                    print('''\
After the tank has faded out you look over at the Lizard Wizard and he winks.'''
                    )
                    _game_state['curr_room']['items'].remove(tank)

                def _b():
                    print('You close the tank to keep the lizard from escaping.')
                    tank.openable_open = False

                def _feed_lizard():
                    print(f'You feed the {tank.lizard.name} lettuce.')
                    for item in inventory:
                        if 'lettuce' in item.name:
                            inventory.remove(item)
                            break
                    sleep(1)
                    print(tank.lizard.trick_text)
                    _b()

                _n()

        Openable.open(self)
        print(f'You see the {self.lizard.name} staring back at you.')
        TankOpen().start(self)
        pass

    def close(self):
        print('The tank is already closed.')
        raise CommandFailed()


class LizardWizardConversation(Scenario):
    hasntmet = True
    got_key = False
    correct = 0

    def start(self, lizardwizard):
        def lwsay(text):
            print(f'LIZARD WIZARD : \"', end='')
            print(text, end='')
            print(f'\"')

        def anything_else():
            lwsay('''\
Was there anything else you wanted to talk about?'''
            )

        def _n():
            self.correct = 0
            choices = []
            choices.append(('Can I have a lizard?', _lizard,))
            choices.append(('How tall are you?', _how_tall,))
            choices.append(('The lizard arcanum', _lizard_arcanum,))
            Scenario.choose(choices)

        def _lizard():
            if self.got_key:
                lwsay('''\
Unfortunately we can\'t go around giving out too many lizards.
Otherwise we would\'nt have any for anyone else who would like to
join the lizard arcanum!'''
                )
                anything_else()
                _n()
            else:
                lwsay('''\
Well of course you can thats what they\'re here for!
But first you must be certified to handle one of our lizards by
joining the lizard arcanum as a junior member.'''
                )
                if _game_state['player'].has_title('Lizard Archwizard'):
                    print('The Lizard Wizard looks up at you and peers at your "Lizard Archwizard" label.')
                    lwsay('''\
Oh i\'m terribly sorry, I did\'nt recognise a superior member in the arcanum.
I am so embarrased.
Go ahead and take any lizard you\'d like, i\'d be extremely honored.'''
                    )
                    print('The Lizard Wizard gives you a key.')
                    self.got_key = True
                    _game_state['player'].state['inventory'].append(LizardKey())
                    return
                lwsay('''\
Would you like to take the certification quiz now?
I can give you some time to study if you\'d like.'''
                )
                choices = []
                choices.append(('Ill take it now', _lizard_one,))
                choices.append(('I\'d like some time to study', _lizard_b,))
                Scenario.choose(choices)

        def _lizard_one():
            lwsay('''\
Ok, first question.
What are the three basic principles of lizard wizardry?'''
            )
            choices = []
            choices.append(('''\
1. Pull the tail first.
2. To open the lizard turn clockwise.
3. The lizard is always right.''', _lizard_one_correct,))
            choices.append(('''\
1. Safety first.
2. The lizard is always right.
3. Respect your lizard and they will bring you greatness.''', _lizard_two,))
            choices.append(('''\
1. Don\'t talk about the lizard arcanum.
2. Don\'t talk about the lizard arcanum.
3. If a lizard makes a noise or rolls over the casting is over.''', _lizard_two,))
            Scenario.choose(choices)

        def _lizard_one_correct():
            self.correct += 1
            _lizard_two()

        def _lizard_two():
            lwsay('''\
Second question.
How do you safely handle a lizard for wizardry?'''
            )
            choices = []
            choices.append(('''Head forwards''', _lizard_three,))
            choices.append(('''Tail forwards''', _lizard_two_correct,))
            choices.append(('''Clockwise''', _lizard_three,))
            Scenario.choose(choices)

        def _lizard_two_correct():
            self.correct += 1
            _lizard_three()

        def _lizard_three():
            lwsay('''\
Now for the third and final question.
What is the landspeed velocity of an unladen lizard?'''
            )
            choices = []
            choices.append(('''1 km/h''', _lizard_check_complete,))
            choices.append(('''5 km/h''', _lizard_three_correct,))
            choices.append(('''10 km/h''', _lizard_check_complete,))
            choices.append(('''African or European?''', _lizard_three_swallow,))
            Scenario.choose(choices)

        def _lizard_three_correct():
            self.correct += 1
            _lizard_check_complete()

        def _lizard_three_swallow():
            lwsay('That is not relevant to the question, I suggest you go study some more.')

        def _lizard_check_complete():
            if self.correct == 0:
                lwsay('''\
You really need to study some more if you\'re going to stand a chance.'''
                )
            elif self.correct == 1:
                lwsay('''\
Hmm not quite, go study some more and come back when you're up
to the challenge.'''
                )
            elif self.correct == 2:
                lwsay('''\
Almost there, go study some more and come back when you're up
to the challenge.'''
                )
            else:
                lwsay('''\
Fantastic!
Let me be the first to welcome you into the lizard arcanum!'''
                )
                print('The Lizard Wizard gives you a key.')
                self.got_key = True
                _game_state['player'].state['inventory'].append(LizardKey())
                _game_state['player'].add_accolade('Lizard Apprentice')

        def _lizard_b():
            lwsay('''\
Ok I\'ll see you back soon enough.'''
            )
            _game_state['player'].add_accolade('The Studious')

        def _how_tall():
            print('''\
The Lizard Wizard stands up out of his chair and crosses his arms.
He\'s even smaller than you thought.'''
            )
            lwsay('''\
Tall enough thank you very much!'''
            )
            print('The Lizard Wizard sits back down.')

        def _lizard_arcanum():
            lwsay('''\
Ahh yes.
It\'s the most prestigous institution of its kind and it spans hundreds of
worlds linking lizard casters together in a brotherhood of green.'''
            )
            anything_else()
            _n()

        if self.hasntmet:
            lwsay('''\
Well hello there!
I am the Lizard Wizard, and it is a pleasure to meet you.'''
            )
            self.hasntmet = False
        else:
            lwsay('Hello again!')
        lwsay('What would you like to talk about?')
        _n()

class LizardWizard(Person):
    name = 'lizard wizard'
    alt_names = ['wizard']
    description = '''\
A strange looking man with a long beard in a long green robe.'''
    scenario = LizardWizardConversation()


herpetology_room = {
    'description': '''\
A small room with a row of tanks along one wall and a large white fridge.
An extremely short man who looks like a wizard is is sitting at a desk
in the corner.''',
    'items': [
        LizardTank(1, DarkLizard()),
        LizardTank(2, BigMouthedLizard()),
        LizardTank(3, SouthernTippedLizard()),
        Fridge()
    ],
    'people': [
        LizardWizard()
    ],
    'exits': {
        'north': RecRoomDoor(),
    }
}
