from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class LinkedinScrapper:

    def __init__(self, username):
        self.username = username

    def __del__(self):
        print("Linkedin Scrapper object is destroyed.")

    def scrape_linkedin_data(self):
        browser = webdriver.Chrome()
        browser.get("https://tr.linkedin.com/in/" + self.username + "/en")
        wait = WebDriverWait(driver=browser, timeout=0)
        follower = (
            wait.until(visibility_of_element_located((By.CSS_SELECTOR, "h3 span")))
        ).text
        connections = (
            wait.until(visibility_of_element_located((By.CLASS_NAME, "top-card__subline-item--bullet")))
        ).text
        browser.close()
        return follower + " " + connections


# Reference
# https://scrapfly.io/blog/scraping-using-browsers/
