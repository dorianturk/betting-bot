# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 17:10:38 2022

@author: Dorian
"""
from PIL import Image
import pyautogui


myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'D:/bot_v2/screenshot_1.png')

def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a

img = 'D:/bot_v2/screenshot_1.png'
memorija = open("D:/bot_v2/memorija.txt", "a")

"""
file1.close()
file1 = open("D:/Python_test/novi/memorija.txt", "a")
"""

for i in range(1757,2082,36):
    for j in range(440,589,25):
        if rgb_of_pixel(img, i, j) == (0, 129, 255):
            memorija.write("plava \n")
            print("pl ",i," ",j)
        elif rgb_of_pixel(img, i, j) == (229, 77, 66):
            memorija.write("crvena \n")
            print("cr ",i," ",j)
        else:
            print("xx ",i," ",j)
            break

memorija.close()