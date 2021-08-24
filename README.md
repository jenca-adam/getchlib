# getchlib - library for reading key presses

## Overview
`getchlib` is library for reading key presses and assigning hotkeys.
### Features
1. Full Unicode support
1. Blocking and non-blocking key press reading
1. Cross-platform support
1. Basic hotkeys ( `CTRL-V` or `ALT-A` ) are defined
1. Not interruptable key press reading support ( cannot be interrupted by `CTRL-C`, returns key code instead )

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
key=getchlib.getkey(False)
```
Returns first key pressed in time specified by its second argument `tout` ( 0.01 by default ).
#### Not interruptable 
```python
import getchlib
key=getchlib.getkey(catch=True)
```
### Hotkeys
```python
import getchlib
def function():
	print('hello')
f=getchlib.HotKeyListener()
f.add_hotkey('ctrl-x',function)
f.start()
```
***NOTE***:*f.start() runs on foreground*
#### Not interruptable
```python
import getchlib
def function():
	print('hello')
f=getchlib.HotKeyListener(catch=True)
f.add_hotkey('a',function)
f.start()
```
## License
*`getchlib` is licensed under* ***GPL License***
