from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from data.country import Country
from data.city import City

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Country, '/country', '/country/<string:name>', endpoint = 'country')
api.add_resource(City, '/city', '/city/<string:name>', endpoint = 'city')

app.run(host= '0.0.0.0', debug=True)