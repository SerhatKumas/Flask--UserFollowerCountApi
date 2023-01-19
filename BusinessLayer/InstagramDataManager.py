# INSTAGRAM MODULE BUSINESS LAYER

# Imports for required modules
from WebScraperLevel.InstragramScrapper import InstagramScrapper
import re


class InstagramDataManager:

    # Initialization method
    def __init__(self, instagram_scraper: InstagramScrapper):
        self.instagram_scraper = instagram_scraper

    # Object destroy method
    def __del__(self):
        print("Instagram Data Manager object is destroyed.")

    # Information string report method
    def follower_count_reporter(self):
        user_stats_string = self.instagram_scraper.scrape_instagram_data()
        print(user_stats_string)
        return user_stats_string

    # Information numbers array method
    def follower_count_array_parser(self):
        user_stats_string = self.instagram_scraper.scrape_instagram_data()
        # With this line we extract all numbers from string and put into array
        user_stats_numbers_array = re.findall('\d+', user_stats_string)
        print(user_stats_numbers_array)
        return user_stats_numbers_array
