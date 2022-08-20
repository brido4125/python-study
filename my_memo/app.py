from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import uuid

client = MongoClient('localhost', 27017)
db = client.myApp
app = Flask(__name__)


class Memo:
    def __init__(self, title, content):
        self.title = title
        self.content = content


memo_list = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['GET'])
def send_data():
    result = list(db.memo.find({}, {'_id': 0}))
    print(result)
    return jsonify({'result': 'success', 'data': result})


@app.route('/memo', methods=['POST'])
def get_data():
    title = request.form.get('title')
    content = request.form.get('content')
    uuid_ = uuid.uuid4()
    memo = {
        'uuid': str(uuid_),
        'title': title,
        'content': content
    }
    db.memo.insert_one(memo)
    return redirect(url_for('home'))


@app.route('/update/memo', methods=['POST'])
def update_memo():
    title = request.form.get('title')
    content = request.form.get('content')
    id = request.form.get('id')
    find_query= {'uuid': id}
    new_values= {'$set':{'title':title,'content':content}}
    db.memo.update_one(find_query,new_values)
    return redirect(url_for('home'))


@app.route('/memo/<id>', methods=['DELETE'])
def delete_memo(id):
    db.memo.delete_one({'uuid': id})
    return redirect(url_for('home'), 'GET')


if __name__ == '__main__':
    app.run()
