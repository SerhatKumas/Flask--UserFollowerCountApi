# LINKEDIN MODULE WEB SCRAPY

# Imports for required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class LinkedinScrapper:

    # Initialization method
    def __init__(self, username):
        self.username = username

    # Object destroy method
    def __del__(self):
        print("Linkedin Scrapper object is destroyed.")

    # Data scraping method
    def scrape_linkedin_data(self):
        browser = webdriver.Chrome()
        # Url creation for getting data
        browser.get("https://tr.linkedin.com/in/" + self.username + "/en")
        # Linked-in is dynamically generated site, so selenium is used for scrapping
        wait = WebDriverWait(driver=browser, timeout=0)
        # Following data getting
        follower = (
            wait.until(visibility_of_element_located((By.CSS_SELECTOR, "h3 span")))
        ).text
        # Connection data getting
        connections = (
            wait.until(visibility_of_element_located((By.CLASS_NAME, "top-card__subline-item--bullet")))
        ).text
        browser.close()
        # Return type is string report
        return follower + " " + connections


# Reference
# https://scrapfly.io/blog/scraping-using-browsers/
