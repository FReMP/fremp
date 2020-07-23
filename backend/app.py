from flask import Flask
from pymongo import MongoClient
import json

app = Flask(__name__)

mongoClient = MongoClient('mongodb://127.0.0.1:27017')
db = mongoClient.get_database('fremp_test_app1_db')
col = db.get_collection('fremp_test_app1_col')

# $ mongo
# $ use fremp_test_app1_db
# $ db.fremp_test_app1_col.insertOne({'data': 'Hello World from MongoDB'})

@app.route('/api/get/')
def getdata():
    data = ''
    if col.find({}):
        for data in col.find({}):
            data = data['data']
    return {'data': data}

if __name__ == "__main__":
    app.run()
