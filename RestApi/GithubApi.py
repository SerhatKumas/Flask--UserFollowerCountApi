from flask import request

from BusinessLayer.GithubDataManager import GithubDataManager
from WebScraperLevel.GithubScrapper import GithubScrapper
from app import app


@app.route('/github-api/follower-report')
def github_follower_count_reporter():
    username = request.args.get("username")

    github_api_controller = GithubDataManager(
        GithubScrapper(username)
    )
    answer = github_api_controller.follower_count_reporter()
    return answer


@app.route('/github-api/follower-array-report')
def github_follower_count_array():
    username = request.args.get("username")

    github_api_controller = GithubDataManager(
        GithubScrapper(username)
    )
    answer = github_api_controller.follower_count_array_parser()
    return answer
