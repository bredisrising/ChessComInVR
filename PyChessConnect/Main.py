import time, mss, socket, threading, json
import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager

PORT = 25001
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

# try:
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect(ADDR)
# except:
#     pass
#make setup.py for setting up things like resolution and chess login


boardToSend = {}

whiteTimer = ""
blackTimer = ""

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

#browser.fullscreen_window()



def startRapid():
    pass
def getTimers():
    pass


def getBoard():
    pieces = browser.find_elements_by_class_name('piece')
    for piece in pieces:
        piece = piece.get_attribute("class").split(" ")
        boardToSend[piece[2][-2:]] = piece[1]

time.sleep(21)

loopTime = time.time()
while True:
    getBoard()
    print("FPS {}".format(1 / (time.time() - loopTime)))
    loopTime = time.time()
    




    


