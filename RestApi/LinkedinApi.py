from flask import request

from BusinessLayer.LinkedinDataManager import LinkedinDataManager
from WebScraperLevel.LinkedinScrapper import LinkedinScrapper
from app import app


@app.route('/linkedin-api/follower-report')
def linkedin_follower_count_reporter():
    username = request.args.get("username")

    linkedin_api_controller = LinkedinDataManager(
        LinkedinScrapper(username)
    )
    answer = linkedin_api_controller.follower_count_reporter()
    return answer


@app.route('/linkedin-api/follower-array-report')
def linkedin_follower_count_array():
    username = request.args.get("username")

    linkedin_api_controller = LinkedinDataManager(
        LinkedinScrapper(username)
    )
    answer = linkedin_api_controller.follower_count_array_parser()
    return answer
