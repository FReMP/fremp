from flask import Flask
from pymongo import MongoClient
import json

app = Flask(__name__)

mongoClient = MongoClient('mongodb+srv://<username>:<password>@cluster0-efer5b.mongodb.net/test?retryWrites=true&w=majority')
db = mongoClient.get_database('fremp_test_app1_db')
col = db.get_collection('fremp_test_app1_col')

# Create an account on MongoDB Atlas
# Add a JSON object to the collection

@app.route('/api/get/')
def getdata():
    data = ''
    if col.find({}):
        for data in col.find({}):
            data = data['data']
    return {'data': data}

if __name__ == "__main__":
    app.run()
