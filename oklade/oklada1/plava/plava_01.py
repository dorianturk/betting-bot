# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:45:02 2022

@author: Dorian
"""

import win32api, win32con
from time import sleep

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
#0,1
click(1750,1275)#ulaz u okladu
sleep(0.5)
click(1750,675)#0,1
sleep(0.25)
#confirme
click(1925,970)
