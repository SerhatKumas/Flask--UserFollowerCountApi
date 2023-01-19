# YOUTUBE MODULE WEB SCRAPY

# Imports for required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class YoutubeScrapper:

    # Initialization method
    def __init__(self, username):
        self.username = username

    # Object destroy method
    def __del__(self):
        print("Youtube Scrapper object is destroyed.")

    # Data scraping method
    def scrape_youtube_data(self):
        # Instantiate options
        options = webdriver.ChromeOptions()
        # Run browser in headless mode
        options.headless = True
        # Instantiate driver
        # Youtube is dynamically generated site, so selenium is used for scrapping
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)
        # Load website
        url = "https://www.youtube.com/@" + self.username
        # Get the entire website content
        driver.get(url)
        # Getting required meta information
        elements = driver.find_elements(By.CLASS_NAME, 'meta-item')
        try:
            # Return type is string
            return elements[2].text
        except Exception as e:
            message = "Youtube channel is not existed with mentioned name"
            print(e)
            # Return type is string report
            return message
