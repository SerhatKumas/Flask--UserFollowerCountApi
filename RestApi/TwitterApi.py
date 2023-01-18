from flask import request
from BusinessLayer.TwitterDataManager import TwitterDataManager
from WebScraperLevel.TwitterScrapper import TwitterScrapper
from app import app


@app.route('/twitter-api/follower-report')
def twitter_follower_count_reporter():
    username = request.args.get("username")

    twitter_api_controller = TwitterDataManager(
        TwitterScrapper(username)
    )
    answer = twitter_api_controller.follower_count_reporter()
    return answer


@app.route('/twitter-api/follower-array-report')
def twitter_follower_count_array():
    username = request.args.get("username")

    twitter_api_controller = TwitterDataManager(
        TwitterScrapper(username)
    )
    answer = twitter_api_controller.follower_count_array()
    return answer
