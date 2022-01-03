import time
import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager


options = uc.ChromeOptions()
options.user_data_dir = "../PyChessConnect/ChromeDataDir"

options.add_argument("--enable-javascript")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

browser = uc.Chrome(ChromeDriverManager().install(), options=options)
time.sleep(2)
browser.get("https://www.chess.com")
time.sleep(3)

time.sleep(100000)




    


