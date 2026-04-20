import keyboard as k
from res import chooser

"""
This file handles the keybinds that are associated with the information
that needs to be typed. Using the built in keyboard function in python
we can bind certains keys to call the function in the other file that 
ultimately leads to writing the info
"""
#jobtitle1
k.add_hotkey('z', chooser, args= ([1]))
#jobtitle2
k.add_hotkey('x', chooser, args= ([2]))
#company1
k.add_hotkey('a', chooser, args= ([3]))
#company2
k.add_hotkey('s', chooser, args= ([4]))
#tdp desc
k.add_hotkey('d', chooser, args= ([5]))
#intern desc
k.add_hotkey('c', chooser, args= ([6]))

k.wait('esc + shift')

