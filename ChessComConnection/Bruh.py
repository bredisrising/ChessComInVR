import undetected_chromedriver.v2 as uc
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
import json, platform, time
from datetime import date, timedelta

if platform.system() == "Darwin":
    #driverPath = r"/Users/ankit/Downloads/chromedriver2"
    driverPath = r"/Users/ankit/Downloads/chromedriver_mac64/chromedriver"
    dataDir = r"/Users/ankit/Desktop/ChessComInVR/ChessComConnection/ChromeDataDir"
elif platform.system() == "Windows":
    driverPath = r"otherBots\microsoftRewardsBot\chromedriver.exe"
    dataDir = r"D:\chrome\User Data - Copy"
else:
    #comment above for linux deployment
    driverPath = r"/home/ankit/Downloads/chromedriver"
    dataDir = r"/var/www/TraderBot/backend/chromedriver"



options = uc.ChromeOptions()

options.user_data_dir = dataDir

options.add_argument("--enable-javascript")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

time.sleep(1)

browser = uc.Chrome(ChromeDriverManager().install(), options=options)
browser.implicitly_wait(3)

browser.get("https://www.google.com")

time.sleep(3000)

browser.quit()

