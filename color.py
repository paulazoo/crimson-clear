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
from env import username, color_password
barcodeD = input("Barcode: ")
numberC = input("Accession number: ")

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

driver.get('https://home.color.com/sign-in?next=%2Fcovid%2Factivation')
#wait to load
time.sleep(3)

driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('password').send_keys(color_password)
driver.find_elements_by_xpath('//button[@type="submit"]')[0].click()
time.sleep(5)
driver.get('https://home.color.com/covid/activation/eligibility')
time.sleep(2)
driver.find_element_by_xpath('//button[@data-testid="No"]').click()
time.sleep(1)
driver.find_element_by_xpath('//button[@data-testid="NextButton"]').click()
time.sleep(1)
driver.find_element_by_xpath('//button[@data-testid="No"]').click()
time.sleep(1)
driver.find_element_by_xpath('//button[@data-testid="NextButton"]').click()
time.sleep(1)
driver.find_element_by_xpath('//span[@data-testid="userAcceptedCheckbox"]').click()
driver.find_element_by_xpath('//span[@data-testid="userHasConsentedCheckbox-0"]').click()
driver.find_element_by_xpath('//span[@data-testid="userHasConsentedCheckbox-1"]').click()
driver.find_element_by_xpath('//span[@data-testid="userHasConsentedCheckbox-2"]').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_xpath('//a[@data-testid="confirm-consent-submit-button"]').click()
time.sleep(1)
driver.find_element_by_xpath('//button[@data-testid="submit-profile-form-button"]').click()
time.sleep(1)
driver.find_element_by_xpath('//button[@data-testid="AcceptAndContinueAction"]').click()
time.sleep(1)
driver.find_element_by_name('kit_barcode').send_keys(barcodeD)
driver.find_element_by_name('accession_number').send_keys(numberC)
driver.find_elements_by_xpath('//button[@type="submit"]')[0].click()
driver.find_element_by_xpath('//button[@data-testid="AcceptAndContinueAction"]').click()
time.sleep(3)
driver.close()



