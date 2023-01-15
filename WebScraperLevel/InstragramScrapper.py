from bs4 import BeautifulSoup
import requests


class InstagramScrapper:

    def __init__(self, username):
        self.username = username

    def __del__(self):
        print("Instagram Scrapper object is destroyed.")

    def scrape_instagram_data(self):
        url = "https://www.instagram.com/" + self.username + "/"
        web_content = requests.get(url)
        soup = BeautifulSoup(web_content.content, features="lxml")
        meta_information = soup.find("meta", {"property": "og:description"}).attrs['content']
        user_stats = meta_information.split("-")[0]
        return user_stats
