from flask import Flask
from flask_restful import Resource, Api
from api import HelloWorld


app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run()
