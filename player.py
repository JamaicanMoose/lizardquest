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
    def has_accolade(self, accolade):
        return accolade in self.state['accolades']

    def add_accolade(self, accolade):
        if not self.has_accolade(accolade):
            self.state['accolades'].append(accolade)
            s = 'New Accolade Acquired! Henceforth, you shall be known as:'
            print('*'*len(s))
            print(s)
            print(f'{self._prettyname}, {accolade}')
            print('*'*len(s))

    def has_title(self, title):
        return title in self.state['titles']

    def add_title(self, title):
        if not self.has_title(title):
            self.state['titles'].append[title]
            s = 'New Title Acquired! Henceforth, you shall be known as:'
            print('*'*len(s))
            print(s)
            print(f'{title} {self._prettyname}')
            print('*'*len(s))

    def examine(self):
        title_str = ' '.join(self.state['titles'])
        accolade_str = ', '.join(self.state['accolades'])
        print(f'You\'re known as {title_str+" " if title_str else ""}{self._prettyname}{", "+accolade_str if accolade_str else ""}.')
