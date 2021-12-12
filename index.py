
from re import A
# crawl a website and click on a link

# import libraries
import time
import os
import requests as req  # for requesting websites
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# get the website
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
wait = WebDriverWait(driver, 100)

# variables for use

channel = 'UCFmmke_oHoQtRSJRbTSbOxA'
webURL = 'https://mytoolstown.com/youtube/earn/'

def page_is_loading(d):
    l = driver.find_element_by_id("actionbtn")
    s = len(l)

    while True:
        x = d.execute_script("return document.readyState")
        if x == "complete" and s > 0:
            return True
        else:
            yield False

def subscribe():
    try:
        getTheCredit = wait.until(EC.element_to_be_clickable(
            (By.ID, "actionbtn")))

        print(getTheCredit.text)

        getTheCredit.send_keys(Keys.ENTER)

        time.sleep(5)
    except TimeoutException:
        subscribe()

def checkLike():
    if page_is_loading(driver):
        try:
            if wait.until(EC.element_to_be_clickable(
                        (By.ID, "actionbtn"))).text == 'LIKE':
                driver.get(webURL)
                time.sleep(10)
                checkLike()
        except TimeoutException:
            driver.get(webURL)
        else:
            l = driver.find_elements_by_id("actionbtn")
            s = len(l)
            if s > 0:
                subscribe()

            try:
                WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
                all_han = driver.window_handles

                if len(all_han) > 1:
                    driver.switch_to.window(all_han[1])
                    driver.close()
                    driver.switch_to.window(all_han[0])

                time.sleep(3)

                if wait.until(EC.element_to_be_clickable(
                        (By.ID, "actionbtn"))).text == 'LIKE':
                    driver.get(webURL)
                else:
                    subscribe()
                    
                checkLike()
            except TimeoutException:
                driver.get(webURL)
                
    else: checkLike()

def crawl():

    result = driver.get(webURL)

    # login to website
    sign_in_link = driver.find_element_by_id('searchbtn')

    inputElement = driver.find_element_by_id("channelid")
    inputElement.send_keys(channel)

    time.sleep(4)

    inputElement.send_keys(Keys.ENTER)
    print(page_is_loading(driver))
    if page_is_loading(driver):
        time.sleep(3)
        driver.get(webURL)

        time.sleep(10)

        checkLike()


    # s = session.post(
    #     "https://mytoolstown.com/youtube/check_account.php", data=payload,  headers=agent)


    # # Navigate to the next page and scrape the data
    # s = session.get('https://mytoolstown.com/youtube/earn/');

    # t = session.get(
    #     'https://mytoolstown.com/youtube/earn/getData.php?kNeT=JKLCM%18HI%19%1A%1FINB%1E%18IMI%1A&type=A')

    # soup = bs(s.text, 'html.parser')

    # text = soup.find('h5', {'class': 'card-title'}).text
    # name = t.json()['fromuser']
    # link = t.json()['link']
    # type = t.json()['type']
    # id = t.json()['promotionid']

    # add href to the button
    # soup.find('a', {'id': 'actionbtn'})['onclick'] = "startwindow('4361759','https://www.youtube.com/channel/UCrG7vaUWXTGrPn0Shdd6n6g?__a=1','Subscribe',2)"

    # print(soup.find('a', {'id': 'actionbtn'})['onclick'])

    # print(text) # print the text
    # print(name) # print the name
    # print(link) # print the link
    # print(type) # print the type
    # print(id) # print the id


if 1 == 1:
    crawl() # run the function