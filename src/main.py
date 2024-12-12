
import board

from kmk.boards.macropact import KMKKeyboard
from kmk.keys import KC, make_key


keyboard = KMKKeyboard()
#keyboard.debug_enabled = True


keyboard.keymap = [
    [KC.LSFT(KC.D), KC.LSFT(KC.I),      KC.S,              KC.LALT(KC.L), KC.LALT(KC.D),       KC.N3,               KC.F2,               KC.N1,
     KC.L,          KC.LCTL(KC.L),      KC.LSFT(KC.L),     KC.LALT(KC.R), KC.LSFT(KC.B),       KC.LSFT(KC.A),       KC.LSFT(KC.E),       KC.LSFT(KC.T),
     KC.LCTL(KC.D), KC.LALT(KC.KP_4),   KC.LALT(KC.KP_6),  KC.NO,         KC.LCTL(KC.B),       KC.LCTL(KC.A),       KC.LCTL(KC.E),       KC.LCTL(KC.T),
     ],
]
   
    
