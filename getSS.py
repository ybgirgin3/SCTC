from pyautogui import screenshot
from imageToText import ittMain
import tempfile as tmp
import numpy as np
import subprocess
import cv2
import os

import notify2 as n2

fn = os.path.join(tmp.gettempdir(), 'temp_ss.png')

def show_notif():
    n2.init("SS to Clipboard for GNU/Linux")
    n = n2.Notification("You can draw the rectangle area, Please make sure target text can readable in your ScreenShot", f"SS path: {fn}")
    n.show()
    

def getSS():
    # full file name
    # create file in tempdir
    os.system(f'scrot --line mode=edge -s -o -f  {fn}')

if __name__ == '__main__':
    # show notification
    show_notif()
    getSS()
    ittMain(fn)
