# INSTAGRAM MODULE WEB SCRAPY

# Imports for required modules
from bs4 import BeautifulSoup
import requests


class InstagramScrapper:

    # Initialization method
    def __init__(self, username):
        self.username = username

    # Object destroy method
    def __del__(self):
        print("Instagram Scrapper object is destroyed.")

    # Data scraping method
    def scrape_instagram_data(self):
        # Url creation for getting data
        url = "https://www.instagram.com/" + self.username + "/"
        # Instagram is not dynamically generated site, so beautiful soap is used for scrapping
        web_content = requests.get(url)
        soup = BeautifulSoup(web_content.content, features="lxml")
        # Meta tag for follower and following information
        meta_information = soup.find("meta", {"property": "og:description"}).attrs['content']
        # Creating array from string information
        user_stats = meta_information.split("-")[0]
        # Return type is array
        return user_stats
