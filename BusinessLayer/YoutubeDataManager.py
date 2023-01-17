from WebScraperLevel.YoutubeScrapper import YoutubeScrapper
import re


class YoutubeDataManager:

    def __init__(self, youtube_scraper: YoutubeScrapper):
        self.youtube_scraper = youtube_scraper

    def __del__(self):
        print("Youtube Data Manager object is destroyed.")

    def follower_count_reporter(self):
        user_stats_string = self.youtube_scraper.scrape_youtube_data()
        print(user_stats_string)
        return user_stats_string

    def follower_count_array_parser(self):
        user_stats_string = self.youtube_scraper.scrape_youtube_data()
        if not user_stats_string.startswith("Youtube"):
            user_stats_string = user_stats_string.split(" ")[0]
        print(user_stats_string)
        return user_stats_string
