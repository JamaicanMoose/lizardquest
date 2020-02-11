from items.item import Item
from items.mixins import Entrance
from person import Person
from scenarios.scenario import Scenario
from time import sleep
from sys import exit

""" The Kitchen
"""

class RecRoomDoor(Entrance, Item):
    name = 'rec room'
    entrance_destination = 'recRoom'
    description = ('A door to the RECREATION ROOM.')

class spaceBacon(Item):
    name = 'bacon'
    description = ('\"SpaceBacon!(tm) Made with RealPig*!\" \n\n'+
                   '*RealPig is a registered trademark of SpaceBacon,'+
                   ' Incorporated. Product may not contain pork products.\n')

class SandwichBuild(Scenario):

    class sandwich(Item):
        name = 'sandwich'
        description = ''

        def __init__(self, sandwichState):
            if sandwichState['open-faced']:
                self.description = ('A delicious looking open-faced %s '
                                    'sandwich, cut into two scrumptious %s' % 
                                    (sandwichState['sauce'], 
                                     sandwichState['cut']))
            else:
                self.description = ('A delicious looking %s sandwich, '
                                    'cut into two scrumptious %s' % 
                                    (sandwichState['sauce'], 
                                     sandwichState['cut']))


    def has_ingredients(self, state):
        lettuce    = False
        bread      = False
        spacebacon = False

        for item in _game_state['player'].state['inventory']:
            if 'lettuce' in item.name:
                lettuce = True
            elif 'bread' in item.name:
                bread = True
            elif 'bacon' in item.name:
                spacebacon = True

        return (lettuce and bread and spacebacon)

    def remove_ingredients(self, state):
        # Bad workaround to deal with array iteration issue: just loop over
        # the array three times
        for item in _game_state['player'].state['inventory']:
            if 'lettuce' in item.name:
                _game_state['player'].state['inventory'].remove(item)
        for item in _game_state['player'].state['inventory']:
            if 'bacon' in item.name:
                _game_state['player'].state['inventory'].remove(item)
        for item in _game_state['player'].state['inventory']:
            if 'bread' in item.name:
                _game_state['player'].state['inventory'].remove(item)

    def alt_convo(self, state):
        print("The chef whistles to himself as he stares at a notepad on "
              "the countertop, listening to some music on his SpacePods.\n"
              "He doesn't seem to notice you, but you notice, in large letters,"
              " the word \"BEANS?\" written at the top of the page.")

    def start(self, state):
        # Run alt scenario if you don't have ingredients
        if not self.has_ingredients(state):
            self.alt_convo(state)
            return

        # Begin the initial scenario
        sandwich = {"open-faced": False,
                    "cut": "",
                    "sauce": ""}

        def _n():
            print("Arming yourself with bread, lettuce, and SpaceBacon, "
                  "you are now ready to realize your ultimate goal.")
            sleep(1)
            print("\n\"Woohoo!\" shouts the chef, pulling out his SpacePods "
                  "and raising his arms in the air.")
            sleep(1)
            print("\nYou begin to assemble the sandwich...")
            sleep(1)

            print("Not so fast! What kind of sandwich is this, anyhow?")
            sandwich["open-faced"] = (Scenario.pick(["A normal sandwich", 
                                                     "Open-faced"]) == 1)

            print("With an image of the sandwich in mind, you begin to "
                  "assemble it.\nYou slap a slice of bread on the chrome "
                  "countertop, layering it with crisp lettuce and a juicy slab "
                  "of SpaceBacon.")
            sleep(2)
            print("Using the tools at your disposal, you prepare to cut the "
                  "sandwich...")
            sleep(1)
            print("...but a shriek pierces the air!")
            sleep(1)
            print("\"Wait!!\" shouts the chef, \"You forgot the sauce!\"\n"
                  "He gestures at the two labeled bottles to your left.")
            sleep(1)

            print("Which sauce do you choose?")
            choices = ["Plurpel Sauce®", "Salt", "No sauce"]
            sandwich["sauce"] = choices[Scenario.pick(choices)]
            if sandwich["sauce"] == "Salt":
                sandwich["sauce"] = "salt"
                print("You choose the bottle labeled \"Salt.\" As far as your "
                      "knowledge of salt goes, this is not it, but you don't "
                      "want to make a fuss.")
                sleep(1)
            elif sandwich["sauce"] == "No sauce":
                sandwich["sauce"] = "sauceless"
                print("The chef looks on as horror as you stare at him and "
                      "proceed, ignoring the sauces...")
                sleep(1)
            else:
                print("The chef smiles, seemingly approving of your sauce "
                      "choice, as you pour the mysteriously-colored sauce on "
                      "your sandwich.")
                sleep(1)

            print("Now, how are you cutting this sandwich anyway?")
            sandwich["cut"] = Scenario.pick(["Triangles", "In half"])
            if sandwich["cut"] == 0:
                sandwich["cut"] = "triangles"
                _game_state['player'].add_accolade('The Triangular')
            else:
                sandwich["cut"] = "rectangles"
                _game_state['player'].add_accolade('The Rectangular')

            if sandwich["open-faced"]:
                print("\nYou cut your sandwich as you see fit. You are now the "
                      "proud owner of an open-faced %s sandwich!\n" % 
                      sandwich["sauce"])
            else:
                print("\nYou cut your sandwich as you see fit. You are now the "
                      "proud owner of a %s sandwich!\n" % sandwich["sauce"])
            self.remove_ingredients(state)

            # Add the sandwich to your inventory
            _game_state['player'].state['inventory'].append(
                self.sandwich(sandwich))

            # sleep(1)
            # print("...")
            # sleep(1)
            # print("...suddenly, you catch yourself off guard, and are briefly "
            #       "blinded by the shining chrome room...")
            # sleep(1)
            # print("...")
            # sleep(1)
            # print("...after regaining your senses, your sandwich is gone!\n"
            #       "You see a butler walking through the door behind you, "
            #       "your sandwich sitting on an illustrious silver platter "
            #       "in his arms.")
            _game_state['player'].add_title('Epicureous')

            # End the game if the player has achieved their goal
            if _game_state['player'].has_accolade('The Hungry'):
                print("\nAs you bite into your sandwich, a feeling of peace "
                      "washes over you...")
                sleep(1)
                print("...pure, unadulterated bliss...")
                sleep(1)
                print("...the way the %s melts into the SpaceBacon can only "
                      "be described as heavenly." % sandwich["sauce"])
                sleep(1)
                print("All your worries wash away, and you don't have a care "
                      "in the world.\nAll that matters is you and your "
                      "sandwich.")
                sleep(3)

                print("\n\nThank you for playing our game! Enter \"0\" when "
                      "you are ready to exit.")
                Scenario.choose([("Bye!", lambda: exit(0))])
            else:
                print("\nAs you bite into your sandwich, you marvel at how "
                      "good it tastes!")
                sleep(1)
                print("With this sandwich at your side, you feel "
                      "well-equipped to tackle your ultimate goal!")


        # Run the scenario    
        _n()

class Chef(Person):
    name = 'chef'
    scenario = SandwichBuild()
    description = f'''\
His head is adorned with a puffy white hat, and he's wearing a stained apron.'''
    alt_names = []

kitchen = {
    'description': ('You are in the KITCHEN.\nThe room smells wonderful,'+
                    'and the shelves are stocked full with all manner of'+
                    ' culinary delights.\nSomeone has left a plate of SPACE'+
                    ' BACON here.\nYou see a CHEF looking at a notepad and'+
                    ' jamming to music.'),
    'items': [
        spaceBacon(),],
    'people': [Chef()],
    'exits': {
        'hubwards': RecRoomDoor(),
    }
}
