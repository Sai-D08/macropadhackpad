from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.matrix.diode_orientation = DiodeOrientation.COL2ROW

keyboard.col_pins = (2, 3, 4)
keyboard.row_pins = (5, 6)

keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
[
KC.LCTRL(KC.C),
KC.LCTRL(KC.V),
KC.LGUI(KC.DOWN),
KC.AUDIO_MUTE,
KC.LGUI(KC.LSFT(KC.S))
]
]

if __name__ == '__main__':
    keyboard.go()
