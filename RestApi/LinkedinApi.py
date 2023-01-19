# LINKEDIN MODULE API

# Imports for required modules
from flask import request
from BusinessLayer.LinkedinDataManager import LinkedinDataManager
from WebScraperLevel.LinkedinScrapper import LinkedinScrapper
from app import app


# End point of string report of information
@app.route('/linkedin-api/follower-report')
def linkedin_follower_count_reporter():
    username = request.args.get("username")

    linkedin_api_controller = LinkedinDataManager(
        LinkedinScrapper(username)
    )
    answer = linkedin_api_controller.follower_count_reporter()
    return answer


# End point of number array of information for further improvements
@app.route('/linkedin-api/follower-array-report')
def linkedin_follower_count_array():
    username = request.args.get("username")

    linkedin_api_controller = LinkedinDataManager(
        LinkedinScrapper(username)
    )
    answer = linkedin_api_controller.follower_count_array()
    return answer
