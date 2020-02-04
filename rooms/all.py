from .room_0_0_0 import room_0_0_0
#from .room_0_0_n1 import room_0_0_n1
from .room_1_0_0 import room_1_0_0
from .bridge import bridge
from .captainsRoom import captainsRoom
from .dorms import dorms
from .escapePods import escapePods
from .haoobam import haoobam
from .herpetologyRoom import herpetologyRoom
from .kitchen import kitchen
from .laundryRoom import laundryRoom
from .stairwell import stairwell
from .upperHall import upperHall
from .zenGarden import zenGarden

## 
## 

rooms = {
    'brig': room_0_0_0,
    'recRoom': room_1_0_0,
    'zenGarden': zenGarden,
    'dorms':dorms,
    'escapePods':escapePods,
    'herpetologyRoom':herpetologyRoom,
    'laundryRoom':laundryRoom,
    'kitchen':kitchen,
    'bridge':bridge,
    'captainsRoom':captainsRoom,
    'HAOoBaM':haoobam,
    'upperHall':upperHall,
    'stairwell':stairwell,
    
    # (0,0,-1): room_0_0_n1
}
