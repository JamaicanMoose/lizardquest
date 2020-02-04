from scenarios.scenario import Scenario
from items.item import Item

class Person(Item):
    name = 'person'
    pronouns = ('they', 'them', 'their', 'theirs', 'themself')
    state = {}
    scenario = Scenario()

    @property
    def prettyname(self):
        return self.name.title()

    def talk(self, state):
        self.scenario.start({'main': state, 'other': self.state})
