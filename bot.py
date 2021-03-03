import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium_driver import SeleniumDriver
from keys import keys
from create_emails import CreateEmail
from spotify_accounts import SpotifyAccount

options = webdriver.ChromeOptions()
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
# options.add_argument('--headless')
driver = SeleniumDriver(webdriver.Chrome(
    ChromeDriverManager().install(), options=options))


if __name__ == '__main__':
    url = keys['google_url']
    # CreateEmail(url, driver)
    SpotifyAccount(keys['spotify_url'], driver)
