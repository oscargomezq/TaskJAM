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
def handle_user():

	if request.method == "POST":
		user_info = request.json
		ret_dict = add_user(db.users, user_info)
		return jsonify(**ret_dict)

@app.route('/task', methods=['POST'])
def handle_task():

	if request.method == "POST":
		task_info = request.json
		ret_dict = add_task(db.tasks, task_info)
		return jsonify(**ret_dict)

@app.route('/match', methods=['POST'])
def handle_match():

	if request.method == "POST":
		match_info = request.json
		ret_dict = make_match(db.tasks, match_info)
		return jsonify(**ret_dict)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)