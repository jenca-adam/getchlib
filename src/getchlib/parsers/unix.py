import re
import enum
from getchlib.key import Key, KeyboardModifier, KeyboardEvent
from typing import TypeVar

KEY_ESCAPE_SS3 = re.compile(r"^O(?P<modifier>\d)?(?P<key>.)")
KEY_ESCAPE_CSI = re.compile(r"^\[(\d;(?P<modifier>\d))?(?P<key>[^~])")
KEY_ESCAPE_CSI2 = re.compile(r"^\[(?P<key>\d+);?(?P<modifier>\d)?;?~")


KEY_ESCAPE_MAPPING = {
    "A": Key.UP,
    "B": Key.DOWN,
    "C": Key.RIGHT,
    "D": Key.LEFT,
    "5": Key.PGUP,
    "6": Key.PGDN,
    "P": Key.F1,
    "Q": Key.F2,
    "R": Key.F3,
    "S": Key.F4,
    "15": Key.F5,
    # 16
    "17": Key.F6,
    "18": Key.F7,
    "19": Key.F8,
    "20": Key.F9,
    "21": Key.F10,
    "22": Key.F11,
    "23": Key.F11,
    "24": Key.F12,
    "\b": Key.BACKSPACE,
    "Z": Key.BACKTAB,
    "3": Key.DELETE,
    "H": Key.HOME,
    "F": Key.END,
    "\n": Key.ENTER,
    "2": Key.INSERT,
    "\x1b": Key.ESC,
    "\t": Key.TAB,
    "\x7f": Key.BACKSPACE,
}

SINGULAR_KEYS = "\x1b\n\b\t\x7f"
CTRL_MAP = {
    chr(ordinal): chr(ordinal + 64)
    for ordinal in range(0, 32)
    if chr(ordinal) not in SINGULAR_KEYS
}


def match_key_code(key_code: str) -> tuple[str, int, int, bool]:
    match = (
        KEY_ESCAPE_SS3.search(key_code)
        or KEY_ESCAPE_CSI2.search(key_code)
        or KEY_ESCAPE_CSI.search(key_code)
    )
    if not match:
        return key_code, 1, len(key_code), False
    groupdict = match.groupdict()
    return groupdict["key"], int(groupdict["modifier"] or 1), match.end() + 1, True


def modifiers_from_bitmask(bitmask: int, modifier_enum: type[enum.IntEnum]) -> set:
    modifiers = set()
    for modifier in modifier_enum:
        if modifier.value & bitmask:
            modifiers.add(modifier)
    return modifiers


def parse_key(code: str) -> tuple[KeyboardEvent | None, int]:
    if not code:
        return (None, 0)
    modifiers = set()
    key: str | Key = code
    end = len(code)
    if code.startswith("\x1b"):
        rest = code[1:]
        matched = False
        if not rest:
            key = Key.ESC
        else:
            key, bitmask, end, matched = match_key_code(rest)
            if not matched:
                key = rest[0]
                modifiers = {KeyboardModifier.ALT}
                end = 2
            else:
                modifiers = modifiers_from_bitmask(bitmask - 1, KeyboardModifier)
        if key in KEY_ESCAPE_MAPPING and matched:
            key = KEY_ESCAPE_MAPPING[str(key)]
    else:
        code = code[:1]
        end = 1
        if code in SINGULAR_KEYS:
            key = KEY_ESCAPE_MAPPING[code]
        else:
            key = code

    if key in CTRL_MAP:
        modifiers.add(KeyboardModifier.CTRL)
        key = CTRL_MAP[str(key)]

    return KeyboardEvent(code[:end], key, modifiers), end
