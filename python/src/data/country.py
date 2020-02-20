from .database_config import DBConfig
from pymongo import MongoClient
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import os

class Country(Resource):

  def __init__(self):
    dbconfig = DBConfig()
    dbconfig.get_db()
    self.client = MongoClient(dbconfig.host)
    self.db = self.client[dbconfig.database]

  def post(self):
    #Clear Countries collection
    self.db.countries.remove({})

    #Open Countries.txt
    f = open(os.path.abspath('../Countries.txt'), "r")
    countries = f.read().splitlines()

    #Insert all countries from file
    for country in countries:
      country = country.split('|')
      dbcountry = {
        'name' : country[0],
        'country_code' : country[1]
      }
      result = self.db.countries.insert_one(dbcountry)
      print('Added {0}, {1} to Country table as {2}'.format(country[0], country[1], result.inserted_id))

    f.close()

    self.client.close()
  
  def get(self, name = None) :
    if name is None :
      countries = self.db.countries.find({})
      result = []
      for field in countries:
        result.append({'id': str(field['_id']), 'name': str(field['name']), 'code': field['country_code']})
      
      return jsonify(result)
    else:
      countries = self.db.countries.find({'name': name})
      result = []
      for field in countries:
        result.append({'id': str(field['_id']), 'name': str(field['name']), 'code': field['country_code']})

      return jsonify(result)

    # def put(self, name):

    # def delete(self, name):