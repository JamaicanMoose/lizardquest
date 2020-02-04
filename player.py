from person import Person

class Player(Person):
    """Holds Relevant data to the current state of the player character"""
    name = 'self'
    _prettyname = ''
    pronouns = ('you', 'you', 'your', 'yours', 'yourself')
    state = {
        'inventory': [],
        'titles': [],
        'accolades': []
    }

    def add_accolade(self, accolade):
        self.state['accolades'].append(accolade)
        print("New Accolade Acquired! Henceforth, you shall be known as:")
        print(f'{self._prettyname}, {accolade}')

    def add_title(self, title):
        self.state['titles'].append[title]
        print("New Title Acquired! Henceforth, you shall be known as:")
        print(f'{title} {self._prettyname}')

    def examine(self):
        title_str = ' '.join(self.state['titles'])
        accolade_str = ', '.join(self.state['accolades'])
        print(f'You\'re known as {title_str+" " if title_str else ""}{self._prettyname}{", "+accolade_str if accolade_str else ""}.')
