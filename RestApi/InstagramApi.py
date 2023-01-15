from flask import request

from BusinessLayer.InstagramDataManager import InstagramDataManager
from WebScraperLevel.InstragramScrapper import InstagramScrapper
from app import app


@app.route('/instagramApi/follower-report')
def ask_question():
    username = request.args.get("username")

    instagram_api_controller = InstagramDataManager(
        InstagramScrapper(username)
    )
    answer = instagram_api_controller.follower_count_reporter()
    return answer


@app.route('/instagramApi/follower-array-report')
def display_answer_repository_config_information():
    username = request.args.get("username")

    instagram_api_controller = InstagramDataManager(
        InstagramScrapper(username)
    )
    answer = instagram_api_controller.follower_count_array_parser()
    return answer
