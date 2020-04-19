# import pandas as pd
from flask import Flask, jsonify, request, render_template
import pymongo
from database import add_user

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
		print (user_info)
		print(type(user_info))

		ret_dict = {"value": "YAY worked"}
		return jsonify(**ret_dict)




if __name__ == '__main__':
    app.run(port = 5000, debug=True)