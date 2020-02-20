from .database_config import DBConfig
from pymongo import MongoClient
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import os
import json

class City(Resource):
  
  def __init__(self):
    dbconfig = DBConfig()
    dbconfig.get_db()
    self.client = MongoClient(dbconfig.host)
    self.db = self.client[dbconfig.database]

  def post(self):
    #Clear Cities collection
    self.db.cities.remove({})
    dbcities = []

    try:
      #Open Cities_X.txt
      for x in range(1, 4):
        f = open(os.path.abspath('../Cities_{0}.txt'.format(x)))
        cities = f.read().splitlines()

        for city in cities:
          city = city.split(',')
          
          dbcity = {
            'country_code' : city[1],
            'city' : city[3].replace('.', '')
          }
          dbcities.append(dbcity)

        f.close()
      
      result = self.db.cities.insert_many(dbcities)
      self.client.close()

      return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    except Exception as e:
      return json.dumps({'Error': str(e)}), 500, {'ContentType':'application/json'} 
    

    

  def get(self, country_code):
    cities = self.db.cities.find({ 'country_code' : country_code })
    result = []
    for field in cities:
      result.append({'id': str(field['_id']), 'name': str(field['name'])})
    
    return jsonify(result)
      
