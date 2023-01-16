from flask import Flask
app = Flask(__name__)

from RestApi import InstagramApi
from RestApi import TiktokApi
from RestApi import LinkedinApi

if __name__ == '__main__':
    app.run()
