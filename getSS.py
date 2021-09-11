from pyautogui import screenshot
from imageToText import ittMain
import tempfile as tmp
import numpy as np
import subprocess
import cv2
import os
from config import *

import notify2 as nt2

fn = os.path.join(tmp.gettempdir(), 'temp_ss.png')

def show_notif(init_str, n1, n2):
    nt2.init(init_str)
    n = nt2.Notification(n1, n2)
    n.show()
    

def getSS():
    # full file name
    # create file in tempdir
    os.system(f'scrot --line mode=edge -s -o -f  {fn}')

if __name__ == '__main__':
    # show notification
    show_notif("SS to Clipboard for GNU/Linux", "You can draw the rectangle area, Please make sure target text can readable in your ScreenShot", f"SS path: {fn}")
    getSS()
    ret = ittMain(fn, tess_path)
    show_notif(init_str="SS to Clipboard for GNU/Linux", n1=f"{ret}", n2="copied to clipboard")

