from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TiktokScrapper:

    def __init__(self, username):
        self.username = username

    def __del__(self):
        print("Tiktok Scrapper object is destroyed.")

    def scrape_tiktok_data(self):
        # instantiate options
        options = webdriver.ChromeOptions()
        # run browser in headless mode
        options.headless = True
        # instantiate driver
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)
        # load website
        url = 'https://www.tiktok.com/@' + self.username
        # get the entire website content
        driver.get(url)
        # select elements by class name tiktok-1kd69nj-DivNumber
        elements = driver.find_elements(By.CLASS_NAME, 'tiktok-1kd69nj-DivNumber')
        answer_array = []
        for elem in elements:
            answer_array.append(elem.find_element(By.TAG_NAME, 'strong').text)
        return answer_array

# Reference
# https://www.zenrows.com/blog/dynamic-web-pages-scraping-python#how-to-scrape-infinite-scroll-web-pages-with-selenium
