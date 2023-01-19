# YOUTUBE MODULE BUSINESS LAYER

# Imports for required modules
from WebScraperLevel.YoutubeScrapper import YoutubeScrapper


class YoutubeDataManager:

    # Initialization method
    def __init__(self, youtube_scraper: YoutubeScrapper):
        self.youtube_scraper = youtube_scraper

    # Object destroy method
    def __del__(self):
        print("Youtube Data Manager object is destroyed.")

    # Information string report method
    def follower_count_reporter(self):
        user_stats_string = self.youtube_scraper.scrape_youtube_data()
        print(user_stats_string)
        return user_stats_string

    # Information numbers array method
    def follower_count_array_parser(self):
        user_stats_string = self.youtube_scraper.scrape_youtube_data()
        # In case of taking error message, separating error message from real data
        if not user_stats_string.startswith("Youtube"):
            # With this line we extract all numbers from string and put into array
            user_stats_string = user_stats_string.split()[0]
        print(user_stats_string)
        return user_stats_string
