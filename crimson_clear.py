import os
from dotenv import load_dotenv

#selenium
from selenium import webdriver
#keyboard manipulation
from selenium.webdriver.common.keys import Keys
#webdriver options
from selenium.webdriver.chrome.options import Options

#keep track of time
import time
#random
import random
#sound notifications (beeps)
import winsound

#to read and edit excel files
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# custom
from cookie_storage import cookies
from helpers import get_cookies

# settings
from env import username, password
new_dual_auth = 0

#set up chrome driver
option = Options()

#stop notif popup
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

#open webdriver chrome browser
driver = webdriver.Chrome(chrome_options=option, executable_path='./chromedriver.exe')
time.sleep(2)

driver.get('https://www.pin1.harvard.edu/cas/login?service=https%3A%2F%2Fcrimsonclear.harvard.edu%2Faccounts%2Flogin%2F%3Fnext%3D%252Fharvard%252Fstart')
#wait to load
time.sleep(3)

# add cookies if already did dual auth
if new_dual_auth == 0:
    for cookie in cookies:
        driver.add_cookie(cookie)
        print('adding cookies...')
    print(driver.get_cookies())

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_name('submit').click()

if new_dual_auth == 1:
    print('Dual authentication loading now...')
    time.sleep(35)
    print('Saving cookies...')
    cookies = get_cookies(driver)
else:
    time.sleep(15)

try:
    driver.find_elements_by_xpath("//a[contains(text(), 'Begin Self-Assessment')]")[0].click()
except:
    driver.get('https://crimsonclear.harvard.edu/harvard/expire_clearance')
    driver.find_elements_by_xpath("//a[contains(text(), 'Begin Self-Assessment')]")[0].click()

time.sleep(2)
driver.find_element_by_xpath('//input[@data-original-value="None"]').click()
time.sleep(2)
driver.find_element_by_xpath('//input[@value="no"]').click()
driver.find_element_by_xpath('//button[@aria-label="Continue"]').click()
time.sleep(2)
driver.find_elements_by_xpath('//input[@value="no"]')[1].click()
driver.find_elements_by_xpath('//button[@aria-label="Continue"]')[1].click()
time.sleep(2)
driver.find_element_by_xpath('//input[@aria-label="Checkbox for attestation"]').click()
driver.find_element_by_xpath('//input[@value="Submit"]').click()
print("Finished crimson clear...")
driver.close()

