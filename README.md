# getchlib - library for reading key presses

## Overview
`getchlib` is library for reading key presses and assigning hotkeys.
**Warning:** update 2.0.0 introduced breaking changes. Please update your code or revert to an earlier version if problems arise.
### Features
- Full Unicode support (Linux only)
- Blocking and non-blocking key press reading
- Cross-platform support
- Support for modifier keys: CTRL, ALT, SHIFT, META. 
- Support for special and function keys.
- Non-interruptable key press reading support ( cannot be interrupted by `CTRL-C`, returns the key instead)
- Fully typed
### Installation
```
pip install getchlib
```
## Usage
### Key Presses
#### Blocking
```python
import getchlib
key=getchlib.getkey()
```
Waits until user presses a key.
#### Non-Blocking
```python
import getchlib
key=getchlib.getkey(blocking=False)
```
Returns the currently pressed key.
On Linux, you can also specify a timeout for the key using the `tout` argument.
#### Non-interruptable 
```python
import getchlib
key=getchlib.getkey(catch=True)
```
#### Buffering
If multiple key presses are registered at the same time, they are stored into an internal buffer. Subsequent calls to `getkey()` read from this buffer. In case this behaviour is not desired, you can force getkey() to read a new key using the `buffer=False` argument.
### KeyboardEvent
`getkey()` returns a `KeyboardEvent` object.
For backwards compatibility, it subclasses `str` - this means that you likely won't have to change your code, if it relied on the old API. 
It has the following attributes:
- `code: str`: the raw key code outputted by the terminal
- `key: getchlib.Key | str`: a member of the `getchlib.Key` enum if it's a special key, a string otherwise.
- `modifiers: {getchlib.KeyboardModifier}`: a set of one of `getchlib.KeyboardModifier.SHIFT`, `getchlib.KeyboardModifier.CTRL`, `getchlib.KeyboardModifier.ALT`, `getchlib.KeyboardModifier.META`
## License
*`getchlib` is licensed under* the ***GPL License***
