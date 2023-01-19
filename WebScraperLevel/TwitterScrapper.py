# TWITTER MODULE WEB SCRAPY

# Imports for required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class TwitterScrapper:

    # Initialization method
    def __init__(self, username):
        self.username = username

    # Object destroy method
    def __del__(self):
        print("Twitter Scrapper object is destroyed.")

    # Data scraping method
    def scrape_twitter_data(self):
        browser = webdriver.Chrome()
        # Url creation for getting data
        browser.get("https://twitter.com/" + self.username)
        # Twitter is dynamically generated site, so selenium is used for scrapping
        wait = WebDriverWait(driver=browser, timeout=10)
        info_array = []
        # Following data
        following = (
            wait.until(visibility_of_element_located((By.XPATH,
                                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span')))
        ).text
        info_array.append(following)
        # Follower data
        follower = (
            wait.until(visibility_of_element_located((By.XPATH,
                                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span')))
        ).text
        info_array.append(follower)
        browser.close()
        # Return type is array
        return info_array

# Reference
# https://scrapfly.io/blog/scraping-using-browsers/
