#!/usr/bin/env python3.6
print ("Welcome to the Automatic Drakensang Online Login Bonus tool.")
import os
import pyautogui
import time

os.startfile('scripts\start.bat')

class Coordinates():
    usrnm = (1255, 346)
    pw = (1250, 382)
    lgn = (1265, 477)
    cr1 = (1651, 278)
    pnow = (1655,984)

def usrnm():
    pyautogui.doubleClick(Coordinates.usrnm)

usrnm()

pyautogui.keyDown('backspace')
pyautogui.keyUp('backspace')

pyautogui.typewrite('YOUR_USER_HERE')

def pw():
    pyautogui.click(Coordinates.pw)

pw()

pyautogui.typewrite('YOUR_PASSWORD_HERE')

def lgn():
    pyautogui.click(Coordinates.lgn)

lgn()

def svr():
    print(pyautogui.click(pyautogui.locateCenterOnScreen('C:\Program Files\Drakensang Online Automatic Login Bonus\imgs\heredur.png')))

svr()
#-------------------------------------------------------------------------------
