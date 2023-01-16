from WebScraperLevel.GithubScrapper import GithubScrapper
import re


class GithubDataManager:

    def __init__(self, github_scraper: GithubScrapper):
        self.github_scraper = github_scraper

    def __del__(self):
        print("Github Data Manager object is destroyed.")

    def follower_count_reporter(self):
        user_stats_string = self.github_scraper.scrape_github_data()
        print(user_stats_string)
        return user_stats_string

    def follower_count_array_parser(self):
        user_stats_string = self.github_scraper.scrape_github_data()
        user_stats_numbers_array = re.findall('\d+', user_stats_string)
        print(user_stats_numbers_array)
        return user_stats_numbers_array
