from random import randint
from time import sleep
from itertools import chain as chain_iter
from player import Player
from rooms.all import rooms
from items.mixins import Openable, Fixed
from scenarios.intro import Intro

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
        print('In the room is:')
        for item in room['items']:
            print(str(item))
    if room['people']:
        pass

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

    inventory = state['player'].inventory
    room_items = rooms[state['curr_room']]['items']
    room_people = rooms[state['curr_room']]['people']
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
                if not isinstance(item, Fixed):
                    inventory.append(item)
                    room_items.remove(item)
                    print(f'You take the {item.name}.')
                    return
                else:
                    print(f'You can\'t take the {item.name}')
                    raise CommandFailed()
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

    def _talk(_to, person):
        if _to != 'to':
            print('What did you want to do?')
            raise CommandFailed()
        if person in room_people:
            person.talk(state)
        else:
            print('Noone named that is here.')
            raise CommandFailed()

    commands = {
        'n': (lambda: _go('north'), 0),
        'ne': (lambda: _go('north east'), 0),
        'e': (lambda: _go('east'), 0),
        'se': (lambda: _go('south east'), 0),
        's': (lambda: _go('south'), 0),
        'sw': (lambda: _go('south west'), 0),
        'w': (lambda: _go('west'), 0),
        'nw': (lambda: _go('north west'), 0),
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
        'look': (_look, 0),
        'talk': (_talk, 2)
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
        'player': Player(),
        'turn': 0,
        'curr_room': (0,0,0)
    }

    Intro().start(state)
    print('\n')
    enter(state['curr_room'])

    while True:
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
