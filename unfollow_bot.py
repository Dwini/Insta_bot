from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = 'C:/Users/aiden/Downloads/chromedriver_win32/chromedriver.exe'
# Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('')
password = webdriver.find_element_by_name('password')
password.send_keys('')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(5)

notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
webdriver.get("https://www.instagram.com/dwini_k/")

for i in range(30):
    time.sleep(10)
    buttons = webdriver.find_elements_by_xpath("//a[@class='-nal3 ']")
    following_button = [button for button in buttons if 'following' in button.get_attribute('href')]
    following_button[0].click()
    time.sleep(20)
    for j in range(10):
        webdriver.find_element_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']").click()
        time.sleep(1)
        webdriver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
        time.sleep(10)
    time.sleep(randint(400,800))
    webdriver.refresh()

