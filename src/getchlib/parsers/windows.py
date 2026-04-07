from getchlib.key import Key, KeyboardModifier, KeyboardEvent

SPECIAL_KEYS = {
    # https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60)
    # WHY is it in a random order
    46: (Key.DELETE, {KeyboardModifier.SHIFT}),
    # GAP
    48: (Key.INSERT, {KeyboardModifier.SHIFT}),
    49: (Key.END, {KeyboardModifier.SHIFT}),
    50: (Key.DOWN, {KeyboardModifier.SHIFT}),
    51: (Key.PGDN, {KeyboardModifier.SHIFT}),
    52: (Key.LEFT, {KeyboardModifier.SHIFT}),
    # GAP
    54: (Key.RIGHT, {KeyboardModifier.SHIFT}),
    55: (Key.HOME, {KeyboardModifier.SHIFT}),
    56: (Key.UP, {KeyboardModifier.SHIFT}),
    57: (Key.PGUP, {KeyboardModifier.SHIFT}),
    # GAP
    59: (Key.F1, set()),
    60: (Key.F2, set()),
    61: (Key.F3, set()),
    62: (Key.F4, set()),
    63: (Key.F5, set()),
    64: (Key.F6, set()),
    65: (Key.F7, set()),
    66: (Key.F8, set()),
    67: (Key.F9, set()),
    68: (Key.F10, set()),
    # GAP
    71: (Key.HOME, set()),
    72: (Key.UP, set()),
    73: (Key.PGUP, set()),
    # GAP
    75: (Key.LEFT, set()),
    # GAP
    77: (Key.RIGHT, set()),
    # GAP
    79: (Key.END, set()),
    80: (Key.DOWN, set()),
    81: (Key.PGDN, set()),
    82: (Key.INSERT, set()),
    83: (Key.DELETE, set()),
    84: (Key.F1, {KeyboardModifier.SHIFT}),
    85: (Key.F2, {KeyboardModifier.SHIFT}),
    86: (Key.F3, {KeyboardModifier.SHIFT}),
    87: (Key.F4, {KeyboardModifier.SHIFT}),
    88: (Key.F5, {KeyboardModifier.SHIFT}),
    89: (Key.F6, {KeyboardModifier.SHIFT}),
    90: (Key.F7, {KeyboardModifier.SHIFT}),
    91: (Key.F8, {KeyboardModifier.SHIFT}),
    92: (Key.F9, {KeyboardModifier.SHIFT}),
    93: (Key.F10, {KeyboardModifier.SHIFT}),
    94: (Key.F1, {KeyboardModifier.CTRL}),
    95: (Key.F2, {KeyboardModifier.CTRL}),
    96: (Key.F3, {KeyboardModifier.CTRL}),
    97: (Key.F4, {KeyboardModifier.CTRL}),
    98: (Key.F5, {KeyboardModifier.CTRL}),
    99: (Key.F6, {KeyboardModifier.CTRL}),
    100: (Key.F7, {KeyboardModifier.CTRL}),
    101: (Key.F8, {KeyboardModifier.CTRL}),
    102: (Key.F9, {KeyboardModifier.CTRL}),
    103: (Key.F10, {KeyboardModifier.CTRL}),
    104: (Key.F1, {KeyboardModifier.ALT}),
    105: (Key.F2, {KeyboardModifier.ALT}),
    106: (Key.F3, {KeyboardModifier.ALT}),
    107: (Key.F4, {KeyboardModifier.ALT}),
    108: (Key.F5, {KeyboardModifier.ALT}),
    109: (Key.F6, {KeyboardModifier.ALT}),
    110: (Key.F7, {KeyboardModifier.ALT}),
    111: (Key.F8, {KeyboardModifier.ALT}),
    112: (Key.F9, {KeyboardModifier.ALT}),
    113: (Key.F10, {KeyboardModifier.ALT}),
    # GAP
    115: (Key.LEFT, {KeyboardModifier.CTRL}),
    116: (Key.RIGHT, {KeyboardModifier.CTRL}),
    117: (Key.END, {KeyboardModifier.CTRL}),
    118: (Key.PGDN, {KeyboardModifier.CTRL}),
    119: (Key.HOME, {KeyboardModifier.CTRL}),
    # GAP
    132: (Key.PGUP, {KeyboardModifier.CTRL}),
    # i want what whoever came up with this scheme is having
    133: (Key.F11, set()),
    134: (Key.F12, set()),
    135: (Key.F11, {KeyboardModifier.SHIFT}),
    136: (Key.F12, {KeyboardModifier.SHIFT}),
    137: (Key.F11, {KeyboardModifier.CTRL}),
    138: (Key.F12, {KeyboardModifier.CTRL}),
    139: (Key.F11, {KeyboardModifier.ALT}),
    140: (Key.F12, {KeyboardModifier.ALT}),
    141: (Key.UP, {KeyboardModifier.CTRL}),
    # GAP
    145: (Key.DOWN, {KeyboardModifier.CTRL}),
    146: (Key.INSERT, {KeyboardModifier.CTRL}),
    147: (Key.DELETE, {KeyboardModifier.CTRL}),
    # GAP
    151: (Key.HOME, {KeyboardModifier.ALT}),
    152: (Key.UP, {KeyboardModifier.ALT}),
    153: (Key.PGUP, {KeyboardModifier.ALT}),
    # GAP
    155: (Key.LEFT, {KeyboardModifier.ALT}),
    # GAP
    157: (Key.RIGHT, {KeyboardModifier.ALT}),
    # GAP
    159: (Key.END, {KeyboardModifier.ALT}),
    160: (Key.DOWN, {KeyboardModifier.ALT}),
    161: (Key.PGDN, {KeyboardModifier.ALT}),
    162: (Key.INSERT, {KeyboardModifier.ALT}),
    163: (Key.DELETE, {KeyboardModifier.ALT}),
}
SINGULAR_KEYS = {8: Key.BACKSPACE, 9: Key.TAB, 13: Key.ENTER, 27: Key.ESC}


def parse_key(code: list[int]) -> tuple[KeyboardEvent | None, int]:
    if not code:
        return None, 0
    key: str | Key = chr(code[0])
    end = 1
    modifiers = set()
    parsing = code[:]
    if parsing[:3] == [24, 64, 115] and len(parsing) >= 4:
        # NOT DOCUMENTED
        modifiers.add(KeyboardModifier.META)
        parsing = parsing[3:]
        end += 3
        key = chr(parsing[0])

    if parsing[0] in (0x00, 0xE0) and len(parsing) >= 2 and parsing[1] in SPECIAL_KEYS:
        key, new_mods = SPECIAL_KEYS[parsing[1]]
        modifiers.update(new_mods)
        end += 1
    elif parsing[0] in SINGULAR_KEYS:
        key = SINGULAR_KEYS[parsing[0]]
    elif 0 < parsing[0] <= 26:  # control key
        key = chr(parsing[0] + 64)
        modifiers.add(KeyboardModifier.CTRL)
    string_code = "".join(chr(i) for i in code[:end])
    return KeyboardEvent(string_code, key, modifiers), end
