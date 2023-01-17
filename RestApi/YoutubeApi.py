from flask import request

from BusinessLayer.YoutubeDataManager import YoutubeDataManager
from WebScraperLevel.YoutubeScrapper import YoutubeScrapper
from app import app


@app.route('/youtube-api/follower-report')
def youtube_follower_count_reporter():
    username = request.args.get("username")

    youtube_api_controller = YoutubeDataManager(
        YoutubeScrapper(username)
    )
    answer = youtube_api_controller.follower_count_reporter()
    return answer


@app.route('/youtube-api/follower-array-report')
def youtube_follower_count_array():
    username = request.args.get("username")

    youtube_api_controller = YoutubeDataManager(
        YoutubeScrapper(username)
    )
    answer = youtube_api_controller.follower_count_array_parser()
    return answer
