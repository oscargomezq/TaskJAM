# import pandas as pd
from flask import Flask, jsonify, request, render_template
import pymongo
from database import add_user, add_task, make_match

# Connect to mongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://oscargomezq:oscargomezq@cluster-taskjam-ahyms.mongodb.net/test?retryWrites=true&w=majority")
db = client["taskjam-db"]


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_user():

	if request.method == "POST":
		user_info = request.json
		ret_dict = add_user(db.users, user_info)
		return jsonify(**ret_dict)

@app.route('/add_task', methods=['POST'])
def add_task():

	if request.method == "POST":
		task_info = request.json
		ret_dict = add_task(db.tasks, task_info)
		return jsonify(**ret_dict)

@app.route('/match', methods=['POST'])
def make_match():

	if request.method == "POST":
		user_info = request.json
		status = make_match(db.users, user_info)
		ret_dict = {"status": status}
		return jsonify(**ret_dict)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)