from imageToText import ittMain
import tempfile as tmp
from config import *
import numpy as np
import subprocess
import argparse
import cv2
import os

import notify2 as nt2



def show_notif(init_str, n1, n2):
    nt2.init(init_str)
    n = nt2.Notification(n1, n2)
    n.show()

def pather(mode: bool):
    if mode:
        fn = os.path.join(f"{save_path}", 'temp_ss.png')
    elif not mode:
        fn = os.path.join(tmp.gettempdir(), 'temp_ss.png')

    return fn



def getSS(fn):
    # full file name
    # create file in tempdir

    os.system(f'scrot --line mode=edge -s -o -f  {fn}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--save", help="Save Screenshot to local drive", action="store_true")
    args = vars(parser.parse_args())

    fn = pather(args['save'])

    ## show notification
    show_notif("SS to Clipboard for GNU/Linux", "You can draw the rectangle area, Please make sure target text can readable in your ScreenShot", f"SS path: {fn}")

    getSS(fn)
    if fn is not None:
        ret = ittMain(fn, tess_path)
    show_notif(init_str="SS to Clipboard for GNU/Linux", n1=f"{ret}", n2="done")

    #print(args['save'])
