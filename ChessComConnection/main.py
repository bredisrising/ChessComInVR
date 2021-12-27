import cv2
import numpy as np
import pyautogui as pg
import time, mss, socket, threading
import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager

PORT = 25001
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

'''
while True:
    time.sleep(1)
    client.sendall("Hello There!".encode("utf-8"))
    recv = client.recv(1024).decode("utf-8")
    print(recv)
'''

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

    for loc in pg.locateAllOnScreen('ChessPieceImages/BlackPawn.png', confidence=.8):
        cv2.rectangle(ss, (loc.left, loc.top), (loc.left+loc.width, loc.top+loc.height), (0, 255, 0), 2)

    ss=cv2.resize(ss, (600, 400))
    cv2.imshow('Vision', ss)

    if(cv2.waitKey(1) == ord('q')):
        cv2.destroyAllWindows()
        break

    


