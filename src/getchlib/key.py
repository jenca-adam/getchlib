import enum


class Key(enum.Enum):
    UP = "Up"
    DOWN = "Down"
    RIGHT = "Right"
    LEFT = "Left"
    PGUP = "PgUp"
    PGDN = "PgDn"
    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F5 = "F5"
    #!!   16
    F6 = "F6"
    F7 = "F7"
    F8 = "F8"
    F9 = "F9"
    F10 = "F10"
    F11 = "F11"
    #!!    23~
    F12 = "F12"
    BACKSPACE = "Backspace"
    BACKTAB = "Backtab"
    DELETE = "Delete"
    HOME = "Home"
    END = "End"
    ENTER = "Enter"
    INSERT = "Insert"
    ESC = "Escape"
    TAB = "Tab"


class KeyboardModifier(enum.IntEnum):
    SHIFT = 1
    ALT = 2
    CTRL = 4
    META = 8


class KeyboardEvent(str):  # to avoid breaking older code
    code: str
    char: str
    key: str | Key
    modifiers: set[KeyboardModifier]

    def __init__(self, code, key, modifiers):
        self.code = code
        self.char = self.code
        self.key = key
        self.modifiers = modifiers

    def __repr__(self):
        return f"<KeyboardEvent key={self.key} modifiers={self.modifiers}>"

    def __new__(cls, code, key, modifiers):
        return super().__new__(cls, code)
