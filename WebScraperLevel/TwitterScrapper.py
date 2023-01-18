from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class TwitterScrapper:

    def __init__(self, username):
        self.username = username

    def __del__(self):
        print("Twitter Scrapper object is destroyed.")

    def scrape_twitter_data(self):
        browser = webdriver.Chrome()
        browser.get("https://twitter.com/" + self.username)
        wait = WebDriverWait(driver=browser, timeout=10)
        info_array = []
        following = (
            wait.until(visibility_of_element_located((By.XPATH,
                                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span')))
        ).text
        info_array.append(following)
        follower = (
            wait.until(visibility_of_element_located((By.XPATH,
                                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span')))
        ).text
        info_array.append(follower)
        browser.close()
        return info_array

# Reference
# https://scrapfly.io/blog/scraping-using-browsers/
