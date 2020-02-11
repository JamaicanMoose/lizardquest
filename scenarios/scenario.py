from time import sleep

class Scenario():

    @staticmethod
    def choose(choices):
        for i, choice in enumerate(choices):
            print(f'[{i}] : {choice[0]}')

        choice = None
        while choice not in range(0,len(choices)):
            try:
                choice_text = input('--? ')
                if choice_text in ('q', 'quit'):
                    exit(0)
                print('')
                choice = int(choice_text)
                if choice not in range(0,len(choices)):
                    raise ValueError()
            except ValueError:
                print('That is not one of your choices.')
        choices[choice][1]()

    # Pick an option, this is just choose without branching
    @staticmethod
    def pick(choices):
        for i, choice in enumerate(choices):
            print(f'[{i}] : {choice}')

        choice = None
        while choice not in range(0,len(choices)):
            try:
                choice_text = input('--? ')
                if choice_text in ('q', 'quit'):
                    exit(0)
                print('')
                choice = int(choice_text)
                if choice not in range(0,len(choices)):
                    raise ValueError()
            except ValueError:
                print('That is not one of your choices.')
        return choice

    def start(self, state):
        pass
