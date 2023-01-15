from WebScraperLevel.TiktokScrapper import TiktokScrapper
import re


class TiktokDataManager:

    def __init__(self, tiktok_scraper: TiktokScrapper):
        self.tiktok_scraper = tiktok_scraper

    def __del__(self):
        print("Tiktok Data Manager object is destroyed.")

    def follower_count_reporter(self):
        user_stats_array = self.tiktok_scraper.scrape_tiktok_data()
        user_stats_string = "Following : " + user_stats_array[0] + " Followers : " + \
                            user_stats_array[1] + " Likes : " + user_stats_array[2]

        print(user_stats_string)
        return user_stats_string

    def follower_count_array(self):
        user_stats_numbers_array = self.tiktok_scraper.scrape_tiktok_data()
        print(user_stats_numbers_array)
        return user_stats_numbers_array
