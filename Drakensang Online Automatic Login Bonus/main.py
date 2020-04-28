from subprocess import *
import pyautogui
import time
import os
import lgn
os.startfile('scripts\start.bat')
time.sleep (1.8)
os.system("lgn.py 1")
time.sleep (5)
Popen('python heredur.py')
