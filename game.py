from random import randint
#from time import sleep
from itertools import chain as chain_iter
from rooms.all import rooms
from items.mixins import Openable

def sleep(i):
    pass

class CommandFailed(Exception):
    pass

def enter(loc):
    room = rooms[loc]
    print(room['description'])
    if room['exits']:
        for direction in room['exits'].keys():
            print(f'To the {direction}: {room["exits"][direction].description}')
    if room['items']:
        print('On the ground is:')
        for item in room['items']:
            print(str(item))

def parser(state, inpt: str):
    comm_inpt = inpt.lower().split()

    def _go(direction):
        room = rooms[state['curr_room']]
        exits = room['exits']
        if direction in exits.keys():
            if exits[direction].destination not in rooms:
                print('DEBUG: That room is not yet implemented!')
                raise CommandFailed()
            if isinstance(exits[direction], Openable):
                if not exits[direction].open:
                    print(f'You can\'t exit through a closed {exits[direction].name}.')
                    raise CommandFailed()
            state['curr_room'] = exits[direction].destination
            enter(state['curr_room'])
        else:
            print('There is no exit in that direction.')
            raise CommandFailed()

    inventory = state['inventory']
    room_items = rooms[state['curr_room']]['items']
    room_exits = rooms[state['curr_room']]['exits'].values()

    def __available_items__():
        return chain_iter(inventory, room_items, room_exits)

    def _examine(item_name):
        for item in __available_items__():
            if item_name.lower() in (item.name.lower(), item.prettyname.lower()):
                item.examine()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _read(item_name):
        for item in __available_items__():
            if item_name.lower() in (item.name.lower(), item.prettyname.lower()):
                item.read()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _take(item_name):
        for item in room_items:
            if item_name.lower() in (item.name.lower(), item.prettyname.lower()):
                inventory.append(item)
                room_items.remove(item)
                print(f'You take the {item.name}.')
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _inventory():
        print('Inventory:\n----------')
        if inventory:
            for item in inventory:
                print(str(item))
        else:
            print('NONE')

    def _look():
        enter(state['curr_room'])

    commands = {
        'n': (lambda: _go('north'), 0),
        's': (lambda: _go('south'), 0),
        'e': (lambda: _go('east'), 0),
        'w': (lambda: _go('west'), 0),
        'go': (_go, 1),
        'examine': (_examine, 1),
        'read': (_read, 1),
        'i': (_inventory, 0),
        'inventory': (_inventory, 0),
        'w': (lambda: None, 0),
        'wait': (lambda: None, 1),
        'take': (_take, 1),
        'q': (lambda: exit(0), 0),
        'quit': (lambda: exit(0), 0),
        'l': (_look, 0),
        'look': (_look, 0)
    }
    if not len(comm_inpt):
        print('What did you want to do?')
        raise CommandFailed()
    comm_name = comm_inpt[0]
    comm_args = comm_inpt[1:]
    if not comm_name in commands:
        print('Thats not something you can do.')
        raise CommandFailed()
    command, num_args = commands[comm_name]
    if num_args == 0 and len(comm_args):
        print(f'You can\'t {comm_name} {" ".join(comm_args)}')
        raise CommandFailed()
    elif num_args < len(comm_args):
        command(*[*comm_args[:num_args-1], ' '.join(comm_args[num_args-1:])])
    elif num_args > len(comm_args):
        print('What did you want to do?')
        raise CommandFailed()
    else:
        command(*comm_args)

def game():
    state = {
        'turn': 0,
        'inventory': [],
        'is_earthquake': True,
        'earthquake_timer': randint(5, 15),
        'curr_room': (0,0,0)
    }

    print('Its dark. The light of your lamp lights your way as you are swallowed by a hole in the forest floor.\nThe sides of the chute you\'ve fallen into transition from earth\n')
    sleep(2)
    print('to stone\n')
    sleep(2)
    print('to flesh\n')
    sleep(1)
    print('as you descend far below.\n')
    sleep(.5)
    print('.\n')
    sleep(.5)
    print('.\n')
    sleep(.5)
    print('.\n')
    print('You land with hardly a sound as the floor below your feet catches you like a thick pillow.\n\nIt\'s warm; and moist.\n\nYour belongings have burst from your knapsack and are spread over the floor.')
    enter(state['curr_room'])

    while True:
        if state['is_earthquake']:
            state['earthquake_timer'] -= 1
            if state['earthquake_timer'] == 0:
                if state['curr_room'] == (0,0,-1):
                    print('A deafaning noise fills the room as the massive hearts beat around you.')
                print('The earth around you trembles...')
                sleep(1)
                state['earthquake_timer'] = randint(5, 15)
        try:
            inpt = input('--> ')
            print('\n')
            parser(state, inpt)
            state['turn'] += 1
        except CommandFailed:
            pass
        print('\n')

if __name__ == '__main__':
    game()
