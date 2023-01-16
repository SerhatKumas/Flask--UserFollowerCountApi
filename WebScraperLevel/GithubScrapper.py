import requests
from bs4 import BeautifulSoup


class GithubScrapper:

    def __init__(self, username):
        self.username = username

    def __del__(self):
        print("Github Scrapper object is destroyed.")

    def scrape_github_data(self):
        url = "https://github.com/" + self.username
        web_content = requests.get(url)
        soup = BeautifulSoup(web_content.content, features="lxml")
        meta_information = soup.findAll("a", {"class": "Link--secondary no-underline no-wrap"})
        follower_info = meta_information[0].text
        following_info = meta_information[1].text
        return " ".join(follower_info.split()) + ' ' + " ".join(following_info.split())
