from flask import Flask, jsonify
from pymongo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps, loads
from mongoengine import connect, ObjectIdField
from models import Qr

app = Flask(__name__)
app.config['DEBUG'] = True


def seedDB():
    qr = Qr.objects(name='testQr').first()
    if not qr:
        Qr(name='testQr', url='www.google.com', data='123data').save()


@app.route("/qrs", methods=['GET'])
def getQRs():
    # GET localhost/qrs
    return jsonify(Qr.objects().to_json())


if __name__ == '__main__':
    connect()
    seedDB()
    app.run()
