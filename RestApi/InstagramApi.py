# INSTAGRAM MODULE API

# Imports for required modules
from flask import request
from BusinessLayer.InstagramDataManager import InstagramDataManager
from WebScraperLevel.InstragramScrapper import InstagramScrapper
from app import app


# End point of string report of information
@app.route('/instagram-api/follower-report')
def instagram_follower_count_reporter():
    username = request.args.get("username")

    instagram_api_controller = InstagramDataManager(
        InstagramScrapper(username)
    )
    answer = instagram_api_controller.follower_count_reporter()
    return answer


# End point of number array of information for further improvements
@app.route('/instagram-api/follower-array-report')
def instagram_follower_count_array():
    username = request.args.get("username")

    instagram_api_controller = InstagramDataManager(
        InstagramScrapper(username)
    )
    answer = instagram_api_controller.follower_count_array_parser()
    return answer
