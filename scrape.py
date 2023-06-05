"""
Scrape data off of Pinterest based on a user given food category
"""

import requests
from bs4 import BeautifulSoup


def user_category():
    """
    Ask the user for what food category they want to do
    a sentiment analysis on.

    This can be multiple categories.
    :return: The food categories given from the user.
    """
    return "food " + input("Enter one or more food categories: ")


def enter_category():
    """
    Enters the categories into the search bar of Pinterest to search for
    the related pins in that category.
    :return: the new url with the specified categories
    """
    return


def main():
    url = "https://www.pinterest.com/"

    # category will contain food at the beginning to increase the
    # probability of searching for food recipes
    category = user_category()


if __name__ == "__main__":
    main()
