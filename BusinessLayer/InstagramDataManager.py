from WebScraperLevel.InstragramScrapper import InstagramScrapper
import re


class InstagramDataManager:

    def __init__(self, instagram_scraper: InstagramScrapper):
        self.instagram_scraper = instagram_scraper

    def __del__(self):
        print("Instagram Data Manager object is destroyed.")

    def follower_count_reporter(self):
        user_stats_string = self.instagram_scraper.scrape_instagram_data()
        print(user_stats_string)
        return user_stats_string

    def follower_count_array_parser(self):
        user_stats_string = self.instagram_scraper.scrape_instagram_data()
        user_stats_numbers_array = re.findall('\d+', user_stats_string)
        print(user_stats_numbers_array)
        return user_stats_numbers_array
