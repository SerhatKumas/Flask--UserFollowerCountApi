# TIKTOK MODULE API

# Imports for required modules
from flask import request
from BusinessLayer.TiktokDataManager import TiktokDataManager
from WebScraperLevel.TiktokScrapper import TiktokScrapper
from app import app


# End point of string report of information
@app.route('/tiktok-api/follower-report')
def tiktok_follower_count_reporter():
    username = request.args.get("username")

    tiktok_api_controller = TiktokDataManager(
        TiktokScrapper(username)
    )
    answer = tiktok_api_controller.follower_count_reporter()
    return answer


# End point of number array of information for further improvements
@app.route('/tiktok-api/follower-array-report')
def tiktok_follower_count_array():
    username = request.args.get("username")

    tiktok_api_controller = TiktokDataManager(
        TiktokScrapper(username)
    )
    answer = tiktok_api_controller.follower_count_array()
    return answer
