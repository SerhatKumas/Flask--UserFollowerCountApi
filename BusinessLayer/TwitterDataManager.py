# TWITTER MODULE BUSINESS LAYER

# Imports for required modules
from WebScraperLevel.TwitterScrapper import TwitterScrapper


class TwitterDataManager:

    # Initialization method
    def __init__(self, twitter_scraper: TwitterScrapper):
        self.twitter_scraper = twitter_scraper

    # Object destroy method
    def __del__(self):
        print("Twitter Data Manager object is destroyed.")

    # Information string report method
    def follower_count_reporter(self):
        user_stats_array = self.twitter_scraper.scrape_twitter_data()
        # With this line we turn number array into string report
        user_stats_string = "Following : " + user_stats_array[0] + " Followers : " + \
                            user_stats_array[1]

        print(user_stats_string)
        return user_stats_string

    # Information numbers array method
    def follower_count_array(self):
        user_stats_numbers_array = self.twitter_scraper.scrape_twitter_data()
        print(user_stats_numbers_array)
        return user_stats_numbers_array
