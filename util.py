from time import sleep

def hasmixin(obj, mixin):
    return issubclass(type(obj), mixin)

def endgame():
    print('**********************')
    print('Thank you for playing!')
    print('**********************')
    print('\n')
    sleep(1)
    print('At the end you were known as:')
    print(_game_state['player'].full_name())
    sleep(1)
    print('Enter q or quit to end the game.')
    while input('--> ') not in ('q', 'quit',):
        pass
    exit()
