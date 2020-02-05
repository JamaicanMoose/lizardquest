from .brig import brig
from .rec_room import rec_room
from .bridge import bridge
from .captains_room import captains_room
from .dorms import dorms
from .escape_pods import escape_pods
from .haoobam import haoobam
from .herpetology_room import herpetology_room
from .kitchen import kitchen
from .laundry_room import laundry_room
from .stairwell import stairwell
from .upper_hall import upper_hall
from .zen_garden import zen_garden

rooms = {
    'brig': brig,
    'recRoom': rec_room,
    'zenGarden': zen_garden,
    'dorms':dorms,
    'escapePods':escape_pods,
    'herpetologyRoom':herpetology_room,
    'laundryRoom':laundry_room,
    'kitchen':kitchen,
    'bridge':bridge,
    'captainsRoom':captains_room,
    'HAOoBaM':haoobam,
    'upperHall':upper_hall,
    'stairwell':stairwell
}

def describe_room(room):
    print(room['description'])
    if room['exits']:
        print("\nPossible exits include:")
        for direction in room['exits'].keys():
            print(f'\t{direction}: {room["exits"][direction].description}')
    if room['items']:
        print('\nA few things catch your eye:')
        for item in room['items']:
            print('\t'+str(item))
    if room['people']:
        pass
