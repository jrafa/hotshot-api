# -*- coding: utf-8 -*-
"""
Module with urls and here run app.
"""
from flask import Flask
from flask_restful import Api
from .api import HotshotsAll, HotshotsOneDay

APP = Flask(__name__)
API = Api(APP)


API.add_resource(HotshotsAll, '/hotshots')
API.add_resource(HotshotsOneDay, '/hotshots/date/<string:date_hotshot>')


if __name__ == '__main__':
    APP.run()
