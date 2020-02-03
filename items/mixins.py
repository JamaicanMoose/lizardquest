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

    locked = False

    def lock(self):
        if not self.locked:
            print(f'You lock the {self.name}.')
            self.locked = True
        else:
            print(f'The {self.name} is already locked.')

    def unlock(self):
        if self.locked:
            print(f'You unlock the {self.name}.')
            self.locked = False
        else:
            print(f'The {self.name} is already unlocked.')

class Openable:
    """Can be opened.
    """

    open = False

    def close(self):
        if self.open:
            print(f'You close the {self.name}.')
            self.open = False
        else:
            print(f'The {self.name} is already closed.')

    def open(self):
        if not self.open:
            print(f'You open the {self.name}.')
            self.open = True
        else:
            print(f'The {self.name} is already open.')

class Breakable:
    """Can be broken.
    """

    broken = False

    def break_(self):
        if self.broken:
            print(f'The {self.name} is already broken.')
        else:
            print(f'The {self.name} breaks.')
            self.broken = False

class Entrance:
    """Can be travelled through.
    """

    destination = (0,0,0)

    def enter(self):
        return self.destination

class Readable:
    """Has text that can be read.
    """

    text = ''

    def read(self):
        print(self.text)
