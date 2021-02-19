import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from test import printWait

options = webdriver.ChromeOptions()
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
#options.add_argument('--headless')

if __name__ == '__main__':
    url = 'https://open.spotify.com/'
    printWait()