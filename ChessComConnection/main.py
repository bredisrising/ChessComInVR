import cv2
import numpy as np
import pyautogui as pg

import time, mss
from selenium import webdriver
import selenium
import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager

#make setup.py for setting up things like resolution and chess login

PIECE_NAMES = ['BlackPawn',
                'WhitePawn',
                'BlackKing',
                'WhiteKing',
                'BlackQueen',
                'WhiteQueen',
                'BlackBishop',
                'WhiteBishop',
                'BlackKnight',
                'WhiteKnight',
                'BlackRook',
                'WhiteRook']


def imgGrab():
    with mss.mss() as instance:
        monitor = instance.monitors[1]
        ss = instance.grab(monitor)
        return ss

options = uc.ChromeOptions()
options.user_data_dir = "ChessComConnection/ChromeDataDir"

options.add_argument("--enable-javascript")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

browser = uc.Chrome(ChromeDriverManager().install(), options=options)
time.sleep(2)
browser.get("https://www.chess.com")
time.sleep(3)

browser.set_window_size(1440, 787)
browser.set_window_position(0, 25)


while(True):
    ss = imgGrab()
    ss = np.array(ss)

    for loc in pg.locateAllOnScreen('BlackPawn.png', confidence=.8):
        cv2.rectangle(ss, (loc.left, loc.top), (loc.left+loc.width, loc.top+loc.height), (0, 255, 0), 2)

    cv2.imshow('Vision', ss)

    if(cv2.waitKey(1) == ord('q')):
        cv2.destroyAllWindows()
        break

    



