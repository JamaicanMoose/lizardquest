from random import randint
from time import sleep
from itertools import chain as chain_iter
from player import Player
from rooms.all import rooms, describe_room
from items.mixins import Openable, Fixed
from scenarios.intro import Intro
from errors import CommandFailed
from util import hasmixin

def sleep(i):
    pass

def parser(inpt: str):
    comm_inpt = inpt.lower().split()

    def _go(direction):
        room = _game_state['curr_room']
        exits = room['exits']
        if direction in exits.keys():
            destination = exits[direction].destination()
            if destination not in rooms:
                print('DEBUG: That room is not yet implemented!')
                raise CommandFailed()
            _game_state['curr_loc'] = destination
            _game_state['curr_room'] = rooms[destination]
            describe_room(_game_state['curr_room'])
        else:
            print('There is no exit in that direction.')
            raise CommandFailed()

    inventory = _game_state['player'].state['inventory']
    room_items = _game_state['curr_room']['items']
    room_people = _game_state['curr_room']['people']
    room_exits = _game_state['curr_room']['exits'].values()

    def __available_items__():
        return chain_iter(inventory, room_items, room_exits)

    def __available__():
        return chain_iter(room_people, __available_items__(), [_game_state['player']])

    def __is_same__(thing_name, thing):
        return thing_name.lower() in (thing.name, thing.prettyname.lower(), *thing.alt_names)

    def _examine(thing_name):
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.examine()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _feel(thing_name):
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.feel()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _read(item_name):
        for item in __available_items__():
            if __is_same__(item_name, item):
                item.read()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _take(item_name):
        for item in room_items:
            if __is_same__(item_name, item):
                if not hasmixin(item, Fixed):
                    inventory.append(item)
                    room_items.remove(item)
                    print(f'You take the {item.name}.')
                    return
                else:
                    print(f'You can\'t take the {item.name}')
                    raise CommandFailed()
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _drop(item_name):
        for item in inventory:
            if __is_same__(item_name, item):
                room_items.append(item)
                inventory.remove(item)
                print(f'You drop the {item.name}')
                return
        print('You aren\'t holding anything like that.')
        raise CommandFailed()

    def _open(thing_name):
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.open()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _close(thing_name):
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.close()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _unlock(thing_name):
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.unlock()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _lock(thing_name):
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.lock()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _turn(onoff, thing_name):
        for thing in __available__():
            if __is_same__(thing_name, thing):
                if onoff == 'on':
                    thing.turn_on()
                elif onoff == 'off':
                    thing.turn_off()
                else:
                    print('What did you want to do?')
                    raise CommandFailed()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _break(thing_name):
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.break_()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _use(thing_name):
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.use()
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
        describe_room(_game_state['curr_room'])

    def _talk(_to, thing_name):
        if _to != 'to':
            print('What did you want to do?')
            raise CommandFailed()
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.talk(_game_state)
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _help():
        command_txt = [
            '(quit, q) : You just can\'t take it anymore.',
            '(help, h) : You should probably know this.',
            '(look, l, surroundings) : Look around the room.',
            '(inventory, i) : Check your inventory.',
            '(go) [DIRECTION] : Take the exit in DIRECTION.',
            '(examine, inspect) [THING] : Get some more information about THING.',
            '(feel, touch) [THING] : Touch THING.',
            '(open) [THING] : Try to open THING.',
            '(close) [THING] : Try to close THING.',
            '(unlock) [THING] : Try to unlock THING.',
            '(lock) [THING] : Try to lock THING.',
            '(turn) [on/off] [THING] : Try to turn THING on/off.',
            '(break) [THING] : Try to break THING.',
            '(use) [THING] : Try to use THING.',
            '(talk) [THING] : Try to talk to THING.',
            '(read) [THING] : Try to read THING.'
            '(wait, w) : Sit around for a bit.'
        ]
        for text in command_txt:
            print(text)

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
        'inspect': (_examine, 1),
        'read': (_read, 1),
        'i': (_inventory, 0),
        'inventory': (_inventory, 0),
        'w': (lambda: None, 0),
        'wait': (lambda: None, 1),
        'take': (_take, 1),
        'drop': (_drop, 1),
        'q': (lambda: exit(0), 0),
        'quit': (lambda: exit(0), 0),
        'l': (_look, 0),
        'look': (_look, 0),
        'surroundings': (_look, 0),
        'talk': (_talk, 2),
        'feel': (_feel, 1),
        'touch': (_feel, 1),
        'open': (_open, 1),
        'close': (_close, 1),
        'unlock': (_unlock, 1),
        'lock': (_lock, 1),
        'turn': (_turn, 2),
        'break': (_break, 1),
        'use': (_use, 1),
        'help': (_help, 0),
        'h': (_help, 0)
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
    # Make game state global
    import builtins
    builtins._game_state = {
        'player': Player(),
        'turn': 0,
        'curr_loc': 'brig',
        'curr_room': rooms['brig']
    }

    Intro().start({})
    print('\n')
    describe_room(_game_state['curr_room'])

    while True:
        try:
            inpt = input('--> ')
            print('\n')
            parser(inpt)
            _game_state['turn'] += 1
        except CommandFailed:
            pass
        print('\n')

if __name__ == '__main__':
    game()
