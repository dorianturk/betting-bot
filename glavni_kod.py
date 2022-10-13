# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 18:14:05 2022

@author: Dorian
"""
import sys
import pyautogui
import cv2
import pytesseract
from time import time, sleep
from PIL import Image
import win32api, win32con


sys.path.append('D:/bot_v2')
memorija = open("D:/bot_v2/memorija.txt", "w")
memorija.close()

brojac_oklade = 0
brojac_oklade_max = 0

def click(x,y):

    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

for br_partija in range(1,105):
    testa=1
    a=time()
    while testa:

        while True:
            try:
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r'screenshot_1.png')       
                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                image = cv2.imread('D:/bot_v2/screenshot_1.png', 0)
                thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]                
                #150% zoom 1440p monitor, desni kut
                x,y,w,h = 2130, 350, 38, 30 
                
                ROI = thresh[y:y+h,x:x+w]
                vrijeme = pytesseract.image_to_string(ROI, lang='eng',config='--psm 6')
                vrijeme10=int(vrijeme)
                break
            except ValueError:
                vrijeme10 = 10
                print("error")
                sleep(4)
        if int(vrijeme10)>47 and int(vrijeme10)<55:
            vrijemeiduce=time()+88
            print (vrijeme," vrijem")
            exec(open("detekcija_boja.py").read())
            click(1710,1363)
            sleep(2)
            click(1920,1363)
            sleep(4)
            
            memorija = open('D:/bot_v2/memorija.txt', "r")
            
            redova = 0
            for br_redova in memorija:
                redova += 1
            print("Podataka u dokumentu memorija:", redova)
            if redova == 0 :
                print ("Dokument je prazan")          
            elif redova == 1 :          
                print ("Trenutno je jedna boja na tabli, cekam 3")         
            elif redova == 2 :
                print ("Trenutno su dvije boje na tabli, cekam 3")
            else:
                red_3 = redova-1
                red_2 = redova-2
                red_1 = redova-3               
                 #print(red_1,red_2,red_3) - test za citanje dokumenta                
                file1 = open('memorija.txt', "r")
                podatak_1=file1.readlines()[red_1]
                file1.close()            
                file1 = open('memorija.txt', "r")
                podatak_2=file1.readlines()[red_2]
                file1.close()             
                file1 = open('memorija.txt', "r")
                podatak_3=file1.readlines()[red_3]
                file1.close()
                             
                if podatak_1 == podatak_2 and podatak_2 == podatak_3:
                    brojac_oklade += 1
                    print("Boja koja se ponavlja je:", podatak_3)
                    print("\nTrenutna oklada:", brojac_oklade)
                    if podatak_3 == 'plava \n' :
                        print("Kladim se na crvenu!")
                        if brojac_oklade == 1 :
                            print("Ulog je: 0,1$")
                            exec(open("D:/bot_v2/oklade/oklada1/crvena/crvena_01.py").read())
                        elif brojac_oklade == 2 :
                            print("Ulog je: 0,3$")
                            exec(open("D:/bot_v2/oklade/oklada1/crvena/crvena_03.py").read())
                        elif brojac_oklade == 3 :
                            print("Ulog je: 0,7$")
                            exec(open("D:/bot_v2/oklade/oklada1/crvena/crvena_07.py").read())
                        elif brojac_oklade == 4 :
                            print("Ulog je: 1,6$")
                            exec(open("D:/bot_v2/oklade/oklada1/crvena/crvena_1_6.py").read())
                        elif brojac_oklade == 5 :
                            print("Ulog je: 3,5$")
                            exec(open("D:/bot_v2/oklade/oklada1/crvena/crvena_3_5.py").read())
                        elif brojac_oklade == 6 :
                            print("Ulog je: 7,5$")
                            exec(open("D:/bot_v2/oklade/oklada1/crvena/crvena_7_5.py").read())
                        elif brojac_oklade == 7 :
                            print("Ulog je: 16$")
                            exec(open("D:/bot_v2/oklade/oklada1/crvena/crvena_17_5.py").read())
                        else:
                            print("Ostao si bez novaca")
                    elif podatak_3 == 'crvena \n' :
                        print("Kladim se na plavu!")
                        if brojac_oklade == 1 :
                            print("Ulog je: 0,1$")
                            exec(open("D:/bot_v2/oklade/oklada1/plava/plava_01.py").read())
                        elif brojac_oklade == 2 :
                            print("Ulog je: 0,3$")
                            exec(open("D:/bot_v2/oklade/oklada1/plava/plava_03.py").read())
                        elif brojac_oklade == 3 :
                            print("Ulog je: 0,7$")
                            exec(open("D:/bot_v2/oklade/oklada1/plava/plava_07.py").read())
                        elif brojac_oklade == 4 :
                            print("Ulog je: 1,6$")
                            exec(open("D:/bot_v2/oklade/oklada1/plava/plava_1_6.py").read())
                        elif brojac_oklade == 5 :
                            print("Ulog je: 3,5$")
                            exec(open("D:/bot_v2/oklade/oklada1/plava/plava_3_5.py").read())
                        elif brojac_oklade == 6 :
                            print("Ulog je: 7,5$")
                            exec(open("D:/bot_v2/oklade/oklada1/plava/plava_7_5.py").read())
                        elif brojac_oklade == 7 :
                            print("Ulog je: 16$")
                            exec(open("D:/bot_v2/oklade/oklada1/plava/plava_17_5.py").read())
                        else:
                            print("Ostao si bez novaca")
                    else:
                        print("Ima greška u kodu!")
                else:
                    print("Trenutna boja je:",podatak_3,"\nPrethodna boja je:", podatak_2)
                    if brojac_oklade <= brojac_oklade_max:
                        brojac_oklade_max = brojac_oklade
                        ponavljanje = brojac_oklade + 2
                    else:
                        brojac_oklade = 0
                        #vamo isklikat home i guessing i u svakom dokumentu oklada ili skontat vamo tipa nakon ocitanja boja pa pauza pa oklada
                        print("Maksimalan broj ponavljanja iste boje:", ponavljanje)

            testa=0
   
        else:
            sleep(4)
            print(vrijeme," nevalja")
    
    sleep(3)
    
    spavanje=vrijemeiduce-time()
    print(spavanje)
    sleep(spavanje)

#cv2.imshow('thresh', thresh)

#cv2.imshow('ROI', ROI)

#cv2.waitKey()"""

"""
ocitavanje timera vraca (rest=time+timer-12)
detekcija boja (if time<rest; elese sleep )
matematika i oklada


ako je oklada dobivena, pokreni nanovo test boje"""