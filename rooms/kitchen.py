from items.item import Item
from items.mixins import Entrance

""" The Kitchen
"""

class RecRoomDoor(Entrance, Item):
    name = 'rec room'
    entrance_destination = 'recRoom'
    description = ('A door to the RECREATION ROOM.')

class spaceBacon(Item):
    name = 'bacon'
    description = ('\"Space Bacon!(tm) Made with RealPig*!\" \n\n'+
                   '*RealPig is a registered trademark of SpaceBacon,'+
                   ' Incorporated. Product may not contain pork products.\n')


kitchen = {
    'description': ('You are in the KITCHEN.\nThe room smells wonderful,'+
                    'and the shelves are stocked full with all manner of'+
                    ' culinary delights.\nSomeone has left a plate of SPACE'+
                    ' BACON here - surely they wouldn\'t ha.'),
    'items': [
        spaceBacon(),],
    'people': [],
    'exits': {
        'hubwards': RecRoomDoor(),
    }
}
