from flask import Flask, jsonify
from pymongo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps, loads
import json

app = Flask(__name__)
app.config['DEBUG'] = True
client = MongoClient()


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient()


@app.route("/qrs", methods=['GET'])
def getQRs():
    db = client.test
    cursor = db.qrs.find({})
    return dumps(cursor)


if __name__ == '__main__':
    connection = Connect.get_connection()
    app.run()
