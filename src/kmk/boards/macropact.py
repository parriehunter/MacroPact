import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    row_pins=(board.GP0, board.GP1, board.GP2),
    column_pins=(board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10),
    diode_orientation = DiodeOrientation.COLUMNS
    coord_mapping = []
    coord_mapping.extend(ic(0, x) for x in range(8))
    coord_mapping.extend(ic(1, x) for x in range(8))
    coord_mapping.extend(ic(2, x) for x in range(8))

    
    
    


