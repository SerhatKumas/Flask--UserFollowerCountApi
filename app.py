from flask import Flask
app = Flask(__name__)

# Imports for connection of end points
# Can be added more when implementations of modules are done
from RestApi import InstagramApi
from RestApi import TiktokApi
from RestApi import GithubApi
from RestApi import YoutubeApi
from RestApi import TwitterApi
from RestApi import LinkedinApi

if __name__ == '__main__':
    app.run()
