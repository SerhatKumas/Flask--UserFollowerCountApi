# TIKTOK MODULE WEB SCRAPY

# Imports for required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TiktokScrapper:

    # Initialization method
    def __init__(self, username):
        self.username = username

    # Object destroy method
    def __del__(self):
        print("Tiktok Scrapper object is destroyed.")

    # Data scraping method
    def scrape_tiktok_data(self):
        # Instantiate options
        options = webdriver.ChromeOptions()
        # Run browser in headless mode
        options.headless = True
        # Tiktok is dynamically generated site, so selenium is used for scrapping
        # Instantiate driver
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)
        # Load website
        url = 'https://www.tiktok.com/@' + self.username
        # Get the entire website content
        driver.get(url)
        # Select elements by class name tiktok-1kd69nj-DivNumber
        elements = driver.find_elements(By.CLASS_NAME, 'tiktok-1kd69nj-DivNumber')
        answer_array = []
        # Selecting required tags for information
        for elem in elements:
            answer_array.append(elem.find_element(By.TAG_NAME, 'strong').text)
        # Return type is array
        return answer_array

# Reference
# https://www.zenrows.com/blog/dynamic-web-pages-scraping-python#how-to-scrape-infinite-scroll-web-pages-with-selenium
