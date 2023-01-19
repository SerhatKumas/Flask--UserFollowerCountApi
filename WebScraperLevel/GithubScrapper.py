# GITHUB MODULE WEB SCRAPY

# Imports for required modules
import requests
from bs4 import BeautifulSoup


class GithubScrapper:

    # Initialization method
    def __init__(self, username):
        self.username = username

    # Object destroy method
    def __del__(self):
        print("Github Scrapper object is destroyed.")

    # Data scraping method
    def scrape_github_data(self):
        # Url creation for getting data
        url = "https://github.com/" + self.username
        # Github is not dynamically generated site, so beautiful soap is used for scrapping
        web_content = requests.get(url)
        soup = BeautifulSoup(web_content.content, features="lxml")
        # Github follower and following info
        meta_information = soup.findAll("a", {"class": "Link--secondary no-underline no-wrap"})
        follower_info = meta_information[0].text
        following_info = meta_information[1].text
        # Return type is string report
        return " ".join(follower_info.split()) + ' ' + " ".join(following_info.split())
