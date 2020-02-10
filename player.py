from person import Person
from scenarios.scenario import Scenario

class TalkToSelf(Scenario):
    num_times_called = 0
    def start(self, state):
        if self.num_times_called == 0:
            self.num_times_called += 1
            print('~~I swear I\'m not going insane~~~')
        elif self.num_times_called == 1:
            self.num_times_called += 1
            print('~~~Maybe I am a bit crazy~~~')
        elif self.num_times_called == 2:
            self.num_times_called += 1
            print('~~~I think someone may be controlling my every action~~~')
        elif self.num_times_called == 3:
            self.num_times_called += 1
            print('~~~Is it you?~~~')
        else:
            self.num_times_called = 1
            print('~~~Who me?~~~')
            state.add_accolade('The Mad')


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
    scenario = TalkToSelf()

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
