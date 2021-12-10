import setuptools

setuptools.setup(
                name='getchlib',
                version='1.0.9',
                description='Library for reading key presses',
                long_description=
'''
# getchlib - library for reading key presses

## Overview
`getchlib` is library for reading key presses and assigning hotkeys.
### Features
1. Full Unicode support
1. Blocking and non-blocking key press reading
1. Cross-platform support
1. Basic hotkeys ( `CTRL-V` or `ALT-A` ) are defined
1. Not interruptable key press reading support ( cannot be interrupted by `CTRL-C`, returns key code instead )
1. Keys as arrow up, arrow left, arrow down, arrow right are defined (for full list, view getchlib.keynames.raw)
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
#### Echo argument (new in v1.0.3)
With `echo=True` characters readed are echoed to the screen.
```python
key=getchlib.getkey(echo=True)

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
''',
        long_description_content_type='text/markdown',
        author='Adam Jenca',
        packages=['getchlib','getchlib.keynames'],
        url='https://pypi.org/project/getchlib/',
        author_email='jenca.a@gjh.sk',
        classifiers=["Development Status :: 3 - Alpha",
                     "Environment :: Console",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: GNU General Public License (GPL)",
                     "Operating System :: OS Independent",
                     "Programming Language :: Python :: 3",
                     ]
    
)
