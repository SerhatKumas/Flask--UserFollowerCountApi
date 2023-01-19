# LINKEDIN MODULE BUSINESS LAYER

# Imports for required modules
from WebScraperLevel.LinkedinScrapper import LinkedinScrapper


class LinkedinDataManager:

    # Initialization method
    def __init__(self, linkedin_scraper: LinkedinScrapper):
        self.linkedin_scraper = linkedin_scraper

    # Object destroy method
    def __del__(self):
        print("Linkedin Data Manager object is destroyed.")

    # Information string report method
    def follower_count_reporter(self):
        user_stats_string = self.linkedin_scraper.scrape_linkedin_data()
        print(user_stats_string)
        return user_stats_string

    # Information numbers array method
    def follower_count_array(self):
        user_stats_string = self.linkedin_scraper.scrape_linkedin_data()
        # With this line we extract all numbers from string and put into array
        user_stats_numbers_array = [user_stats_string.split()[0], user_stats_string.split()[2]]
        print(user_stats_numbers_array)
        return user_stats_numbers_array
