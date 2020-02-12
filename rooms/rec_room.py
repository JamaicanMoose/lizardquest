from items.item import Item
from items.mixins import Entrance, Fixed

""" RecRoom
"""

class toBrig(Entrance, Item):
    name = 'ladder'
    entrance_destination = 'brig'
    description = 'A ladder to the ship\'s BRIG.'

class toHerpetology(Entrance, Item):
    name = 'door to the herpetology room'
    entrance_destination = 'herpetologyRoom'
    description = 'A door to the ship\'s HERPETOLOGY LAB.'

class toDorms(Entrance, Item):
    name = 'door to the dorms'
    entrance_destination = 'dorms'
    description = 'A door to the ship\'s DORM annex.'

class toZen(Entrance, Item):
    name = 'door to the zen garden'
    entrance_destination = 'zenGarden'
    description = 'A door to the ship\'s ZEN GARDEN.'

class toStairwell(Entrance, Item):
    name = 'staircase'
    entrance_destination = 'stairwell'
    description = 'An extremely fancy STAIRCASE leading upwards.'

class toKitchen(Entrance, Item):
    name = 'kitchen'
    entrance_destination = 'kitchen'
    description = 'A door to the ship\'s KITCHEN.'

class RoomRoom(Fixed, Item):
    name='door to Room.'
    alt_names = ['room', 'room.']
    description=('You notice something peculiar. There\'s a door here'+
                 'just labeled \"Room.\" The door is locked.\n'+
                 'In fact, it seems as though someone has intentionally broken'+
                 'the unlock-panel.\nYou can\'t really see why- it\'s just'+
                 ' a normal-looking door for a normal-seeming room.\n'+
                 '...\n...\n...\n...\nAs you begin to turn away, something'+
                 ' seems to move in the corner of your eye.\n'+
                 'For the briefest second, you could swear you saw through the door.\n'+
                 'And on the other side...\n'+
                 'Movement?\nBlood?\nTeeth?\nWhatever it was, it certainly '+
                 'wasn\'t a normal body, and that certainly wasn\'t a normal Room.\n'+
                 'There is a soft scratching coming from the other side, and you\'re'+
                 ' glad the lock is engaged.\nYou understand why the Room. is off limits.\n'+
                 'You suddenly understand what it took to close it.\nThe sacrifices that were made.\n'+
                 'You won\'t forget. You can\'t forget.\nYou turn around to leave and-\n\n\n-huh. That\'s weird.\nThere are tears on your cheeks!\n'+
                 'You can\'t remember seeing anything that sad recently... weird.\n'+
                 'As far as you can remember, you\'ve just been standing in the center of the REC ROOM.\n'+
                 'One one of the walls, there\'s a room just labeled \"Room.\"\n'+
                 'You make a note to check it out later- weird that you haven\'t already investigated it!')

class LizardBrothel(Fixed, Item):
    name='door to the lizard brothel'
    alt_names = ['lizard brothel', 'brothel']
    description=('Oh, no. You\'re not going in there.\nNot after the incident'+
                 ' at the last lizard brothel you went to.')

class LizaRnD(Fixed, Item):
    name='door to lizard research and development'
    alt_names = ['lizard research', 'research', 'development']
    description=('Behind this door is the cutting edge of research into'+
                 'lizards and lizard-care acoutrements.\nThe door displays a'+
                 ' holographic message: \"Testing in Progress. Do Not Disturb.\"'+
                 '\nThe door is locked and tightly sealed, but from behind it,'+
                 ' you can hear the sounds of lasers and heavy machinery,'+
                 ' punctuated by the cheers of elated scientists.\n'+
                 ' You wait for an hour to see if the testing will stop'+
                 ' for even a few moments- just enough to get your foot in the '+
                 'door, to see what\'s going on in there...\n...But alas, the door remains closed and locked from the inside.')
## A button would exist here that lets you jettison Lizard RnD into space,
## meant to only be activated in an emergency. It has text that implies
## that it unlocks the door. If the player activates it, then on future visits
## there is no longer any sound from behind the door, as the entire room
## has decoupled and become its own, smaller ship. The player gets the accolade
## Emergency Quarantine Officer (or, if we want to be mean, Enemy of Science)

class JustSoup(Fixed, Item):
    name='door to just soup'
    alt_names = ['soup', 'just soup']
    description=('To the north-east side of the room, you notice'+
                 ' the familiar branding of Just Soup, '+
                 'a pretty mediocre chain restaurant.\nA holo-screen informs you that the'+
                 ' restaurant is currently closed for renovations.\n'+
                 'Normally, when the restaurant is closed, you can order'+
                 ' from the auto-vendor attached to the outside window...\n'+
                 '...but the machine\'s display currently reads \"Error: Just Plain Broken\",'+
                 ' which isn\'t the best indicator of usability.\nAh, well. No big loss. You wanted a sandwich, anyways.\n')

class TVArea(Fixed, Item):
    name = 'TV area'
    description=('An absolute monster of a couch is positioned in front of\n'+
                 'an equally large television.\nA stand of holo-discs sits '+
                 'nearby, and you quickly scan some of the titles-\n\"King of the'+
                 'Belly-button Piercing: Brotherhood of the Stud\"\n'+
                 '\"We Legally Can\'t Call This Despicable Me\"\n'+
                 '\"Star Wars Episode IV: A New Hope\"- that last one strikes'+
                 ' you as odd. Who would put a grim, serious documentary in with'+
                 ' all these comedies?\nIn any case, you\'ve seen all these '+
                 'before, and don\'t really feel like revisiting the classics.\n'+
                 'You walk back to the center of the room.')

rec_room = {
    'description': ('You are in the REC ROOM, also known as the RECREATION ROOM.\n'+
                    'By far the largest room on the ship, it seems to serve as '+
                    'a sort of central hub of activity.\nHolo-projectors create dazzling lightshows'+
                    ' as smooth jazz plays over the speakers.\nYou can smell something delicious coming'+
                    ' from the KITCHEN and the DORMS, and you can hear the sounds of mist being sprayed in the HERPETOLOGY ROOM.\n'),
    'items': [TVArea(),
              JustSoup(),
              RoomRoom(),
              LizaRnD(),
              LizardBrothel()],
    'people': [],
    'exits': {
        'down': toBrig(),
        'up': toStairwell(),
        'lizardwards': toHerpetology(),
        'foodwards': toKitchen(),
        'bedwards': toDorms(),
        'zenwards': toZen(),
    }
}
