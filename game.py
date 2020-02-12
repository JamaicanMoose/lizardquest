from random import randint
from time import sleep
from itertools import chain as chain_iter
from player import Player
from rooms.all import rooms, describe_room
from items.mixins import Openable, Readable, Lockable
from scenarios.intro import Intro
from errors import CommandFailed
from util import hasmixin

def sleep(i):
    pass

def parser(inpt: str):
    comm_inpt = inpt.lower().split()

    def _go(direction):
        prev_loc = _game_state['curr_loc']
        room = _game_state['curr_room']
        exits = room['exits']
        if direction in exits.keys():
            exit = exits[direction]
            destination = exit.destination()
            if hasmixin(exit, Openable) and not exit.openable_open:
                print(f'You can\'t go there, the {exit.entrance_type} is shut tightly.')
                raise CommandFailed()

            if destination not in rooms:
                print('DEBUG: That room is not yet implemented!')
                raise CommandFailed()
            new_room = rooms[destination]
            _game_state['curr_loc'] = destination
            _game_state['curr_room'] = new_room
            # Replace exit names with new information about where they go
            exit._entrance_replace_name()
            for exit in new_room['exits'].values():
                if exit.destination() == prev_loc:
                    exit._entrance_replace_name()
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

    def _prompt_for_thing(thing_name, action):
        if thing_name:
            return thing_name
        else:
            print(f'What would you like to {action}?')
            return input('--? ')

    def _examine(thing_name):
        thing_name = _prompt_for_thing(thing_name, 'examine')
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.examine()
                if hasmixin(thing, Readable):
                    print('It Reads:')
                    thing.read()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _feel(thing_name):
        thing_name = _prompt_for_thing(thing_name, 'feel')
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.feel()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _read(item_name):
        item_name = _prompt_for_thing(item_name, 'read')
        for item in __available_items__():
            if __is_same__(item_name, item):
                item.read()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _take(item_name):
        item_name = _prompt_for_thing(item_name, 'take')
        for item in room_items:
            if __is_same__(item_name, item):
                if item.can_take:
                    inventory.append(item)
                    room_items.remove(item)
                    print(item.take_text)
                    return
                else:
                    print(item.take_fail_text)
                    raise CommandFailed()
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _drop(item_name):
        item_name = _prompt_for_thing(item_name, 'drop')
        for item in inventory:
            if __is_same__(item_name, item):
                room_items.append(item)
                inventory.remove(item)
                print(f'You drop the {item.name}')
                return
        print('You aren\'t holding anything like that.')
        raise CommandFailed()

    def _open(thing_name):
        thing_name = _prompt_for_thing(thing_name, 'open')
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.open()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _close(thing_name):
        thing_name = _prompt_for_thing(thing_name, 'close')
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.close()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _unlock(thing_name):
        thing_name = _prompt_for_thing(thing_name, 'unlock')
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.unlock()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _lock(thing_name):
        thing_name = _prompt_for_thing(thing_name, 'lock')
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.lock()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _turn(onoff, thing_name):
        if onoff not in ('on', 'off'):
            print(f'What does it even mean to turn something {onoff}?')
            raise CommandFailed()
        thing_name = _prompt_for_thing(thing_name, f'turn {onoff}')
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
        thing_name = _prompt_for_thing(thing_name, 'break')
        for thing in __available__():
            if __is_same__(thing_name, thing):
                thing.break_()
                return
        print('Nothing like that exists here.')
        raise CommandFailed()

    def _use(thing_name):
        thing_name = _prompt_for_thing(thing_name, 'use')
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
                thing.talk()
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
            '(examine, x, inspect) [THING] : Get some more information about THING.',
            '(feel, touch) [THING] : Touch THING.',
            '(open) [THING] : Try to open THING.',
            '(close) [THING] : Try to close THING.',
            '(unlock) [THING] : Try to unlock THING.',
            '(lock) [THING] : Try to lock THING.',
            '(turn) [on/off] [THING] : Try to turn THING on/off.',
            '(break) [THING] : Try to break THING.',
            '(use) [THING] : Try to use THING.',
            '(talk to) [ENTITY] : Try to talk to ENTITY.',
            '(read) [THING] : Try to read THING.',
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
        'u': (lambda: _go('up'), 0),
        'd': (lambda: _go('down'), 0),
        'go': (_go, 1),
        'examine': (_examine, 1),
        'x': (_examine, 1),
        'inspect': (_examine, 1),
        'read': (_read, 1),
        'i': (_inventory, 0),
        'inventory': (_inventory, 0),
        'wait': (lambda: None, 1),
        'take': (_take, 1),
        'get': (_take, 1),
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
        filler = [None]*(num_args-len(comm_args))
        command(*[*comm_args, *filler])
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
