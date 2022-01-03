import time, socket, json
from threading import Thread
import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager

PORT = 25001
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


'''
while True:
    try:
        client.connect(ADDR)
    except:
        print("FAILED TO CONNECT TO: " + SERVER + "\n ...TRYING AGAIN...")
        time.sleep(2)
        continue
'''

client.connect(ADDR)

#make setup.py for setting up things like resolution and chess login

#TRY PUTTING IN MAIN FUNCTION AND CALLING BELOW

options = uc.ChromeOptions()
options.user_data_dir = "../PyChessConnect/ChromeDataDir"

options.add_argument("--enable-javascript")
#options.add_argument("--disable-blink-features")
#options.add_argument("--disable-blink-features=AutomationControlled")

browser = uc.Chrome(ChromeDriverManager().install(), options=options)
time.sleep(2)
browser.get("https://www.chess.com")
time.sleep(2)
browser.find_element_by_id("quick-link-computer").click()
time.sleep(1.5)

if len(browser.find_elements_by_class_name('piece')) <= 0:
    browser.find_element_by_css_selector("body > div.layout-sidebar.sidebar > div.selection-menu-component > div.selection-menu-footer > button").click()
    time.sleep(1)
    browser.find_element_by_css_selector("body > div.layout-sidebar.sidebar > div.selection-menu-component > div.selection-menu-footer > button").click()

#browser.fullscreen_window()

time.sleep(5)

boardToSend = {}

playingAsWhite = 0

#NOTE boardToSend[piece[2][-2:]] = piece[1] causing uncommon list index out of range error
#NOTE unity might not be deserializing correctly
#NOTE RESEARCH EXACTLY WUT JSON STRING IS

def getBoard():
    while True:
        boardToSend.clear()
        pieces = browser.find_elements_by_class_name('piece')
        for piece in pieces:
            piece = piece.get_attribute("class").split(" ")
            boardToSend[piece[2][-2:]] = piece[1]
        senderData = json.dumps(boardToSend)
        print(senderData.encode("utf-8"))
        client.sendall(senderData.encode("utf-8"))
        time.sleep(.5)


def getTimers():
    whiteTimerElement = browser.find_element_by_class_name("clock-white").find_element_by_tag_name("span")
    blackTimerElement = browser.find_element_by_class_name("clock-black").find_element_by_tag_name("span")
    while True:
        whiteTimer = whiteTimerElement.text
        blackTimer = blackTimerElement.text
        client.sendall(("1 " + whiteTimer).encode("utf-8"))
        client.sendall(("0 " + blackTimer).encode("utf-8"))
        time.sleep(.5)


boardProcess = Thread(target=getBoard)
timerProcess = Thread(target=getTimers)

boardProcess.start()
#timerProcess.start()

boardProcess.join()
#timerProcess.join()


    




    


