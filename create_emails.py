import random
from password_generator import PasswordGenerator

firstNames = []
lastNames = []
pwo = PasswordGenerator()
pwo.minlen = 8

with open('data/firstnames.txt') as first_names:
    for name in first_names:
        firstNames.append(name)
    first_names.close()

with open('data/lastnames.txt') as last_names:
    for name in last_names:
        lastNames.append(name)
    last_names.close()

def CreateEmail(url, driver):
    rand_num = random.randint(0, 5000)
    firstName = firstNames[rand_num]
    lastName = lastNames[rand_num].lower()
    email = f'{firstName}.{lastName}{rand_num}'
    password = pwo.generate()

    driver.get(url)
    driver.sendKeys(firstName, 'firstName')
    driver.sendKeys(lastName, 'lastName')
    driver.sendKeys(email, 'username')
    driver.sendKeys(password, 'passwd')
    driver.sendKeys(password, 'ConfirmPasswd')
