"""
Scrape data off of Pinterest based on a user given food category

Resources:
https://stackoverflow.com/questions/68330937/typing-text-into-a-search-box-when-using-selenium-and-beautiful-soup-in-python
https://www.geeksforgeeks.org/interacting-with-webpage-selenium-python/?ref=lbp

to look at:
https://stackoverflow.com/questions/48225334/extracting-data-from-pinterest-using-beautifulsoup-python
https://github.com/mjdall/pinterest_scraper/blob/master/pinterest_scraper.py
"""
import msvcrt
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import maskpass
import time

def user_category():
    """
    Ask the user for what food category they want to do
    a sentiment analysis on.

    This can be multiple categories.
    :return: The food categories given from the user.
    """
    return "food " + input("Enter one or more food categories separated by a space: ")


def enter_category(driver, category):
    """
    Enters the categories into the search bar of Pinterest to search for
    the related pins in that category.
    :param category:
    :return: the new url with the specified categories
    """
    search_bar = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="searchBoxContainer"]/div/div/div[2]/input')))

    if not search_bar:
        raise RuntimeError("Could not find search bar.")

    search_bar.send_keys(category)
    search_bar.send_keys(Keys.ENTER)


def get_username_and_pass():
    """TODO: find a more secure way of doing this"""
    email = input("Email: ")
    password = input("Password: ")
    return (email, password)

def log_in(driver, credentials):
    """
        Find the login button on Pinterest, click it and ask user to type in their username and password.
        :param driver:
        :return:
        """
    # log in
    login_element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="fullpage-wrapper"]/div[1]/div/div/div[1]/div//div[2]/div[2]/button/div')))

    if not login_element:
        raise RuntimeError("Could not find login button.")

    # click on login button
    login_element.click()

    email = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'email')))
    password = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password')))

    if not email or not password:
        raise RuntimeError("Could not find email or password input boxes.")

    # enter users email and password
    email.send_keys(credentials[0])
    password.send_keys(credentials[1])

    # enter user credentials into login
    submit_credentials = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div[2]/div/div/div/div/div/div[4]/form/div[7]')))
    if not submit_credentials:
        raise RuntimeError("Could not submit login credentials.")
    submit_credentials.click()


def main():
    url = "https://www.pinterest.ca/"

    # get users email and password to log in
    credentials = get_username_and_pass()

    # category will contain food at the beginning to increase the
    # probability of searching for food recipes
    category = user_category()

    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # get pinterest.ca
    driver.get(url)

    # log in to Pinterest
    log_in(driver, credentials)

    enter_category(driver, category)

    time.sleep((60))
    driver.quit()


if __name__ == "__main__":
    main()
