from .item import Item
from .mixins import Stateful, Breakable

class Lamp(Stateful, Breakable, Item):
    name = 'lamp'

    def __str__(self):
        return f'A Lamp' + {' (Broken)' if self.broken else ''} + {' (Lit)' if self.on else ''}

    @property
    def description(self):
        strs = ['Its a cheap lamp, the store in town sold it to you.']
        if self.broken:
            strs.append('You seem to have broken it.')
        if self.on:
            strs.append('It seems to be lit.')
        return ' '.join(strs)

    def feel(self):
        strs = ['The metal housing feels smooth and cold in your hands.']
        if self.on:
            strs.append('Heat radiates outward from the lamp.')
        print(''.join(strs))

    def turn_on(self):
        if self.on:
            print('The lamp is already lit.')
        else:
            if not self.broken:
                print('The lamp lights up.')
                self.on = True
            else:
                print('The lamp is broken.')

    def turn_off(self):
        if self.on:
            print('The lamp darkens.')
            self.on = False
        else:
            print('The lamp is already dark.')

    def break_(self):
        if self.broken:
            print('The lamp is already broken.')
        else:
            if self.on:
                print('The lamp cracks and the light goes out.')
                self.on = False
            else:
                print('The lamp cracks.')
            self.broken = True
