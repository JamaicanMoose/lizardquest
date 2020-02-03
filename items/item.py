from abc import ABC

class Item(ABC):

    name = 'thing'

    def __str__(self):
        return f'A {self.name.title()}'

    _prettyname = None

    def getpn(self):
        if not self._prettyname:
            self._prettyname = str(self)
        return self._prettyname

    def setpn(self, new):
        self._prettyname = new

    prettyname = property(getpn, setpn)

    @property
    def description(self):
        return f'It is definitely a {self.name}. Looking closer you see more of its {self.name}ness.'

    def examine(self):
        print(self.description)

    def feel(self):
        print(f'Definitely feels like a {self.name}.')

    def open(self):
        print(f'This thing is not one of the things that can be opened.')

    def close(self):
        print(f'This thing is not one of the things that can be closed.')

    def unlock(self):
        print(f'This thing is not one of the things that can be unlocked.')

    def lock(self):
        print(f'This thing is not one of the things that can be locked.')

    def turn_on(self):
        print(f'What does it even mean to turn on a {self.name}?')

    def turn_off(self):
        print(f'What does it even mean to turn off a {self.name}?')

    def break_(self):
        print(f'The {self.name} cannot be broken.')

    def read(self):
        print(f'There is no text on it.')

    def enter(self):
        print(f'What does it even mean to enter a {self.name}?')
