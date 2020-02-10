from abc import ABC
from errors import CommandFailed

class Item(ABC):

    name = 'thing'
    alt_names = tuple([])
    pronouns = ('it', 'it', 'its', '', 'itself')

    @property
    def prettyname(self):
        return f'A {self.name.title()}'

    def __str__(self):
        return self.prettyname

    @property
    def description(self):
        return f'It is definitely {self.prettyname}. Looking closer you see more of {self.pronouns[2]} {self.name}ness.'

    def examine(self):
        print(self.description)

    def feel(self):
        print(f'Definitely feels like {self.prettyname}.')

    def open(self):
        print(f'This thing is not one of the things that can be opened.')
        raise CommandFailed()

    def close(self):
        print(f'This thing is not one of the things that can be closed.')
        raise CommandFailed()

    def unlock(self):
        print(f'This thing is not one of the things that can be unlocked.')
        raise CommandFailed()

    def lock(self):
        print(f'This thing is not one of the things that can be locked.')
        raise CommandFailed()

    def turn_on(self):
        print(f'What does it even mean to turn on a {self.name}?')
        raise CommandFailed()

    def turn_off(self):
        print(f'What does it even mean to turn off a {self.name}?')
        raise CommandFailed()

    def break_(self):
        print(f'The {self.name} cannot be broken.')

    def read(self):
        print(f'There is no text on it.')

    def destination(self):
        print(f'Where does a {self.name} go?')
        raise CommandFailed()

    def use(self):
        print(f'What does it even mean to use a {self.name}?')
        raise CommandFailed()

    def talk(self):
        print(f'Talking to inanimate objects now are we?')
        raise CommandFailed()

    can_take = True

    @property
    def take_text(self):
        return f'You take the {self.name}.'

    @property
    def take_fail_text(self):
        return f'You can\'t take the {self.name}'
