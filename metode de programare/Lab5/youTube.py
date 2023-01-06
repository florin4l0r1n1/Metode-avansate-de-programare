#pip3 install pyautogui
#pip3 install time
#pip3 install keyboard
#pip3 install pywin32
#pip3 install pytesseract

import pyautogui
import time
import keyboard
import webbrowser


webbrowser.open("https://youtube.com")

pozitie_initiala_x = 556
pozitie_initiala_y = 840

def cautare_google():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'/home/florin/Documents/f.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'/home/florin/Documents/f.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('https://youtube.com')
        pyautogui.press('enter')
    else:
        print("Imagine nu este pe ecran")

cautare_google()

def cautare_youtube():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'/home/florin/Documents/ff.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'/home/florin/Documents/ff.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('George Buhnici')
        pyautogui.press('enter')
    else:
        print("Imagine nu este pe ecran")

cautare_youtube()

def cautare_canal():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'/home/florin/Documents/search.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'/home/florin/Documents/search.png', confidence=0.7)
        pyautogui.click(camp_google)
    else:
        print("Imagine nu este pe ecran")

cautare_canal()

def abonare():
    time.sleep(4)
    if pyautogui.locateOnScreen(r'/home/florin/Documents/abonare.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'/home/florin/Documents/abonare.png', confidence=0.7)
        pyautogui.click(camp_google)
    else:
        print("Esti abonat.")

abonare()

def videoclipuri():
    time.sleep(1)
    if pyautogui.locateOnScreen(r'/home/florin/Documents/video.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'/home/florin/Documents/video.png', confidence=0.7)
        pyautogui.click(camp_google)
    else:
        print("Imagine nu este pe ecran")

videoclipuri()

def coordonate():
    print(pyautogui.position()) #scrie pozitia cursorului pe ecran

i = 0
while ((i <= 3) and not keyboard.is_pressed('esc')):
    time.sleep(1)
    pyautogui.click(pozitie_initiala_x, pozitie_initiala_y)
    time.sleep(5)
    pyautogui.click(28,61)
    time.sleep(1)
    pyautogui.click(28,81)
    time.sleep(1)
    pozitie_initiala_x += 300
    i = i + 1


