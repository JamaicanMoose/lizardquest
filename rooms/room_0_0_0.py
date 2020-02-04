from items.item import Item
from items.mixins import Entrance, Openable, Readable, Fixed

""" The Brig [Room (0,0,0)]
"""

class Ladder(Entrance, Item):
    name = 'ladder'
    destination = 'recRoom'
    description = ('A sturdy chrome ladder.')

##class Grate(Entrance, Openable, Item):
##    name = 'grate'
##    open = False
##    destination = (0,0,-1)
##
##    @property
##    def description(self):
##        return 'A Large Stone Grate' + (' (Open)' if self.open else ' (Closed)')

class EmployeeBoard(Fixed, Item):
    name = 'grid of photos'
    description = ('As you get closer, you realize that every photo in the grid depicts the same person.\n'+
                   'Sixty pictures of the guard stare back at you, each one prouder and more enthusiastic than the last.\n'+
                   'Beneath each is a simple metal plaque - \"Employee of the Month\".')
                   

class Medal(Fixed, Readable, Item):
    name = 'medal'
    text='\"The Department of Bureaucracy and Mail recognizes the recipient of this medal as a Good and Special Boy.\"'
    description = ('The guard holds what appears to be a gold star, polished to a mirror sheen.\n'+
                   'It reads \"The Department of Bureaucracy and Mail recognizes the recipient of this medal as a Good and Special Boy.\"\n'+
                   'On the back, the words \"You Performed Adequately!\" are printed in Comic Sans, followed by a ridiculous amount of fine print.'+
                   '\nThe guard sniffs, teary-eyed and smiling with pride, as he shows it to you.\n'+
                   'He doesn\'t look willing to give it to you, and given how focused he is, it doesn\'t seem like taking it is an option.')


room_0_0_0 = {
    'description': ('You find yourself in the ship\'s BRIG.\n'+
                    'Vacant cells line either side of the central hall.'+
                    '\nOn the NORTH side of the hall,'+
                    ' a ladder extends upwards, presumably leading '+
                    'to the second floor of the ship.\nA small '+
                    'sign off to the side of the ladder '+
                    'reads \"To Rec Room.\"\n'
                    '\nOn the other end of the hall, there is a GRID OF'+
                    ' PHOTOS.\n'
                    '\nA guard sits in the middle of the hall, proudly polishing a MEDAL of some'+
                    ' fashion.'),
    'items': [
        EmployeeBoard(),
        Medal()
    ],
    'people': [],
    'exits': {
##        'south': Grate(),
        'north': Ladder(),
    }
}
