from WebScraperLevel.TwitterScrapper import TwitterScrapper


class TwitterDataManager:

    def __init__(self, twitter_scraper: TwitterScrapper):
        self.twitter_scraper = twitter_scraper

    def __del__(self):
        print("Twitter Data Manager object is destroyed.")

    def follower_count_reporter(self):
        user_stats_array = self.twitter_scraper.scrape_twitter_data()
        user_stats_string = "Following : " + user_stats_array[0] + " Followers : " + \
                            user_stats_array[1]

        print(user_stats_string)
        return user_stats_string

    def follower_count_array(self):
        user_stats_numbers_array = self.twitter_scraper.scrape_twitter_data()
        print(user_stats_numbers_array)
        return user_stats_numbers_array
