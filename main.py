chrome_driver = "C:/Users/91892/PycharmProjects/selerium_driver/chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

date = datetime.datetime.now()
date = date.date()
URL = "https://twitter.com/login"
URL_speed = "https://www.speedtest.net/"

driver = webdriver.Chrome(chrome_driver)
driver.maximize_window()
driver.get(URL_speed)
driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
time.sleep(60)
speed_text =driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]')
strings=list(speed_text.text.split("\n"))
driver.quit()
Your_password = ""
YOUR_MAIL_ID = ""
driver = webdriver.Chrome(chrome_driver)
driver.maximize_window()
driver.get(URL)
time.sleep(6)
google_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
google_button.send_keys(YOUR_MAIL_ID)
google_button.send_keys((Keys.ENTER))
time.sleep(5)
passw = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
passw.send_keys(Your_password)
passw.send_keys(Keys.ENTER)
time.sleep(6)
post_tweet  = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
post_tweet.click()
post_tweet.send_keys(f"My Jio Prepaid speed on {date} is\n{[f'{strings[i]}={strings[i+1]}' for i in range(0,5,2)]}.Kindly note it's sending from Kolkata location." )
post = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span').click()
driver.quit()

