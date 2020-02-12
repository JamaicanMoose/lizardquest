from errors import CommandFailed
from util import hasmixin
from .item import Item

class Stateful:
    """Can be turned on and off.
    """

    on = False

    def turn_on(self):
        if self.on:
            print(f'You turn on the {self.name}.')
            self.on = True
        else:
            print(f'The {self.name} is already on.')

    def turn_off(self):
        if not self.on:
            print(f'You turn off the {self.name}.')
            self.on = False
        else:
            print(f'The {self.name} is already off.')

class Lockable:
    """Can be locked.
    """

    lockable_locked = False

    def lock(self):
        if not self.lockable_locked:
            if hasmixin(self, Openable) and self.openable_open:
                print(f'You can\'t lock an open {self.name}.')
                raise CommandFailed()
            print(f'You lock the {self.name}.')
            self.lockable_locked = True
        else:
            print(f'The {self.name} is already locked.')
            raise CommandFailed()

    def unlock(self):
        if self.lockable_locked:
            print(f'You unlock the {self.name}.')
            self.lockable_locked = False
        else:
            print(f'The {self.name} is already unlocked.')
            raise CommandFailed()


class Breakable:
    """Can be broken.
    """

    broken = False

    def break_(self):
        if self.broken:
            print(f'The {self.name} is already broken.')
            raise CommandFailed()
        else:
            print(f'The {self.name} breaks.')
            self.broken = False


class Readable:
    """Has text that can be read.
    """

    text = ''

    def read(self):
        print(self.text)


class Entrance(Readable):
    """Can be travelled through.
    """

    entrance_destination = (0,0,0)
    entrance_destination_name = ''
    entrance_type = ''
    entrance_verb = 'go through'
    entrance_examined = False
    prettyname = ''

    def __init__(self):
        self.prettyname = self.name.title()

    def destination(self):
        return self.entrance_destination

    @property
    def text(self):
        return f'\"To {self.entrance_destination_name.title()}\"'

    def _entrance_replace_name(self):
        if not self.entrance_examined:
            self.alt_names.append(self.name)
            self.alt_names.append(self.entrance_destination_name)
            self.name = f'{self.entrance_type} to {self.entrance_destination_name}'
            self.prettyname = self.name.title()
            self.entrance_examined = True

    def examine(self):
        self._entrance_replace_name()
        Item.examine(self)


class Openable:
    """Can be opened.
    """

    openable_open = False

    def close(self):
        if self.openable_open:
            print(f'You close the {self.name}.')
            self.openable_open = False
        else:
            print(f'The {self.name} is already closed.')
            raise CommandFailed()

    def open(self):
        if not self.openable_open:
            if hasmixin(self, Lockable) and self.lockable_locked:
                if hasmixin(self, Entrance):
                    print(f'You can\'t open a locked {self.entrance_type}.')
                else:
                    print(f'You can\'t open a locked {self.name}.')
                raise CommandFailed()
            print(f'You open the {self.name}.')
            self.openable_open = True
        else:
            print(f'The {self.name} is already open.')
            raise CommandFailed()


class Fixed:
    """Cannot be taken or moved.
    """
    can_take = False
