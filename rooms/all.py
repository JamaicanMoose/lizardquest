from .room_0_0_0 import room_0_0_0
#from .room_0_0_n1 import room_0_0_n1
from .room_1_0_0 import room_1_0_0

rooms = {
    (0,0,0): room_0_0_0,
    (1,0,0): room_1_0_0,
    # (0,0,-1): room_0_0_n1
}

def describe_room(room):
    print(room['description'])
    if room['exits']:
        for direction in room['exits'].keys():
            print(f'To the {direction}: {room["exits"][direction].description}')
    if room['items']:
        print('In the room is:')
        for item in room['items']:
            print(str(item))
    if room['people']:
        pass
