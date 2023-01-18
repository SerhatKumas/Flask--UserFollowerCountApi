from WebScraperLevel.LinkedinScrapper import LinkedinScrapper


class LinkedinDataManager:

    def __init__(self, linkedin_scraper: LinkedinScrapper):
        self.linkedin_scraper = linkedin_scraper

    def __del__(self):
        print("Linkedin Data Manager object is destroyed.")

    def follower_count_reporter(self):
        user_stats_string = self.linkedin_scraper.scrape_linkedin_data()
        print(user_stats_string)
        return user_stats_string

    def follower_count_array(self):
        user_stats_string = self.linkedin_scraper.scrape_linkedin_data()
        user_stats_numbers_array = [user_stats_string.split()[0], user_stats_string.split()[2]]
        print(user_stats_numbers_array)
        return user_stats_numbers_array
