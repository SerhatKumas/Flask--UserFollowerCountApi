from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class YoutubeScrapper:

    def __init__(self, username):
        self.username = username

    def __del__(self):
        print("Youtube Scrapper object is destroyed.")

    def scrape_youtube_data(self):
        # instantiate options
        options = webdriver.ChromeOptions()
        # run browser in headless mode
        options.headless = True
        # instantiate driver
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)
        # load website
        url = "https://www.youtube.com/@" + self.username
        # get the entire website content
        driver.get(url)
        elements = driver.find_elements(By.CLASS_NAME, 'meta-item')
        try:
            return elements[2].text
        except Exception as e:
            message = "Youtube channel is not existed with mentioned name"
            print(e)
            return message
