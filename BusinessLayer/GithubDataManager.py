# GITHUB MODULE BUSINESS LAYER

# Imports for required modules
from WebScraperLevel.GithubScrapper import GithubScrapper
import re


class GithubDataManager:

    # Initialization method
    def __init__(self, github_scraper: GithubScrapper):
        self.github_scraper = github_scraper

    # Object destroy method
    def __del__(self):
        print("Github Data Manager object is destroyed.")

    # Information string report method
    def follower_count_reporter(self):
        user_stats_string = self.github_scraper.scrape_github_data()
        print(user_stats_string)
        return user_stats_string

    # Information numbers array method
    def follower_count_array_parser(self):
        user_stats_string = self.github_scraper.scrape_github_data()
        # With this line we extract all numbers from string and put into array
        user_stats_numbers_array = re.findall('\d+', user_stats_string)
        print(user_stats_numbers_array)
        return user_stats_numbers_array
