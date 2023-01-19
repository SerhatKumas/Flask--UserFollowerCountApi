# TIKTOK MODULE BUSINESS LAYER

# Imports for required modules
from WebScraperLevel.TiktokScrapper import TiktokScrapper


class TiktokDataManager:

    # Initialization method
    def __init__(self, tiktok_scraper: TiktokScrapper):
        self.tiktok_scraper = tiktok_scraper

    # Object destroy method
    def __del__(self):
        print("Tiktok Data Manager object is destroyed.")

    # Information string report method
    def follower_count_reporter(self):
        user_stats_array = self.tiktok_scraper.scrape_tiktok_data()
        # With this line we turn number array into string report
        user_stats_string = "Following : " + user_stats_array[0] + " Followers : " + \
                            user_stats_array[1] + " Likes : " + user_stats_array[2]

        print(user_stats_string)
        return user_stats_string

    # Information numbers array method
    def follower_count_array(self):
        user_stats_numbers_array = self.tiktok_scraper.scrape_tiktok_data()
        print(user_stats_numbers_array)
        return user_stats_numbers_array
