# GITHUB MODULE API

# Imports for required modules
from flask import request
from BusinessLayer.GithubDataManager import GithubDataManager
from WebScraperLevel.GithubScrapper import GithubScrapper
from app import app


# End point of string report of information
@app.route('/github-api/follower-report')
def github_follower_count_reporter():
    username = request.args.get("username")

    github_api_controller = GithubDataManager(
        GithubScrapper(username)
    )
    answer = github_api_controller.follower_count_reporter()
    return answer


# End point of number array of information for further improvements
@app.route('/github-api/follower-array-report')
def github_follower_count_array():
    username = request.args.get("username")

    github_api_controller = GithubDataManager(
        GithubScrapper(username)
    )
    answer = github_api_controller.follower_count_array_parser()
    return answer
