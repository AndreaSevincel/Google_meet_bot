from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pause
import pynput
import os
from pynput.keyboard import Key, Controller
from datetime import datetime
#######YEAR#MONTH#DAY#HOUR#MINUTE###### DO NOT PUT ZERO BEFORE A NUMBER
# MAIL & PASSWORD (THE MAIL U WILL USE TO ENTER TO THE MEET)
driver = webdriver.Chrome(
    r'C:\Users\user\OneDrive\Masaüstü\bot project\chromedriver.exe')
usernameStr = 'yourr mail'
passwordStr = 'your_password'
url_meet = 'https://meet.google.com/lookup/d7eskmr7pd'
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=800,600")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 2
})
browser = webdriver.Chrome(chrome_options=options)
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))
username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(2)
keyboard = Controller()
#keyboard.type(passwordStr)
password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
password.send_keys(passwordStr)
#keyboard.type(passwordStr)
signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
time.sleep(2)
browser.get(url_meet)
time.sleep(2)
element = browser.find_element_by_class_name('CwaK9')
browser.execute_script("arguments[0].click();", element)
browser.find_element_by_xpath(
    "//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
pause
