import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium_driver import SeleniumDriver
import random 
from keys import keys


options = webdriver.ChromeOptions()
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
#options.add_argument('--headless')
driver = SeleniumDriver(webdriver.Chrome(options=options))
selenium_Driver = SeleniumDriver(driver) 

firstNames = []
lastNames = []

with open('firstnames.txt') as first_names:
  for name in first_names:
    firstNames.append(name)

with open('lastnames.txt') as last_names:
  for name in last_names:
    lastNames.append(name)
    

def create_email(url):
  rand_num = random.randint(0,5000)
  email = f'{firstNames[rand_num]}.{lastNames[rand_num]}{rand_num}@gmail.com'

  driver.get(url)
  driver.sendKeys(firstNames[rand_num], 'firstName')

if __name__ == '__main__':
  url = keys['google_url']
  create_email(url)