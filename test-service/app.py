from flask import Flask, request
from flask_restful import Resource, Api
import requests
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")

db = client.aNewDB
userNum = db['userNum']
userNum.insert({'num_of_users': 0})

class Customer(Resource):
    def get(self):
        prev_num = int(userNum.find({})[0]['num_of_users']) + 1
        userNum.update({}, {'$set':{'num_of_users' : prev_num}})
        return {
                "name" : "Khizar",
                "address" : "36 capel road",
                "accounts": 4,
                "v_id": prev_num
                }
    def post(self):
        body = request.get_json(force=True)
        return body

api.add_resource(Customer, "/customer")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")



