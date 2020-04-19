import pymongo
import random
from datetime import datetime 
from datetime import timedelta
# import pandas as pd
import json
from bson import json_util

# user is a python dict
def add_user (collection, user):
	
	# Parse user json info
	ret_dict = {}
	try:
		ret_dict['msg'] =  "Succesfully registered user " + user['first_name'] + " " + user['last_name']
		ret_dict['status_code'] = 200
		# Insert to db
		collection.insert_one(user)
	except:
		ret_dict['msg'] = "Error registering user"
		ret_dict['status_code'] = 400
	return ret_dict

# task is a python dict
def add_task (collection, task):
	
	# Parse user json info
	ret_dict = {}
	try:
		ret_dict['msg'] =  "Succesfully registered task " + task['description'] + " for user " + task['username']
		ret_dict['status_code'] = 200
		# Insert to db
		collection.insert_one(task)
	except:
		ret_dict['msg'] = "Error adding task"
		ret_dict['status_code'] = 400
	return ret_dict

def make_match(collection, match):
	
	ret_dict = {}
	try:
		ret_dict['msg'] =  "Succesfully matched task " + match['description'] + " for user " + match['username']
		ret_dict['status_code'] = 200
	except:
		ret_dict['msg'] = "Error matching user"
		ret_dict['status_code'] = 400

	username = match['username']
	# Find match
	match_username = 'john_doe_123'
		
	ret_dict['matched_with'] = match_username

	return ret_dict

def init_datasets():
	
	first_df = pd.read_csv('names/first_names.csv', header=None)
	print(first_df.head())
	first_names = first_df.iloc[:,0].tolist()
	first_names = [x.strip().split(" ")[0] for x in first_names]

	last_df = pd.read_csv('names/last_names.csv', header=None, usecols=[0])
	print(last_df.head())
	last_names = last_df.iloc[:,0].tolist()
	last_names = [x.strip().split(" ")[0] for x in last_names]

	hobbies_df = pd.read_csv('names/hobbies.csv')
	print(hobbies_df.head())
	interests = hobbies_df.iloc[:,0].tolist()

	return first_names, last_names, interests

def generate_username(first_name, last_name, usernames):
	n = 0
	username = first_name.lower() + "_" + last_name.lower() + "_" + str(n)
	while (username in usernames):
		n += 1
		username = first_name.lower() + "_" + last_name.lower() + "_" + str(n)
	return username

def random_date_of_birth():
    """Generate a random datetime between `start` and `end`"""
    start = datetime.strptime('1/1/1960 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime('1/1/2006 1:30 PM', '%m/%d/%Y %I:%M %p') 
    return start + timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

# Create csv with mock user data
def populate_user_collection (collection, n_users = 100000):

	# https://github.com/smashew/NameDatabases/tree/master/NamesDatabases/
	# https://www.kaggle.com/muhadel/hobbies/version/3
	# Generate names dicts from the datasets above

	first_names, last_names, interests = init_datasets()
	usernames = set({})
	mail_hosts = ["hotmail", "gmail", "outlook", "yahoo"]
	languages = ["English", "Arabic", "Spanish"]

	# Final list of users with details, each user a dict
	users = []

	for i in range(n_users):

		new_user = {}

		new_user['first_name']  = random.choice(first_names)
		new_user['last_name'] = random.choice(last_names)

		new_user['username'] = generate_username(new_user['first_name'], new_user['last_name'], usernames)
		new_user['email'] = new_user['username'] + "@" + random.choice(mail_hosts) + ".com"

		new_user['languages'] = random.sample(languages, k = random.choice(range(len(languages))) + 1 )
		new_user['interests'] = random.sample(interests, k = random.choice(range(10)) + 1 )

		new_user['date_of_birth'] = random_date_of_birth()

		users.append(new_user)

		if (i%10000)==1 or i==n_users-1:
			collection.insert_many(users)
			users = []

	# users_df = pd.DataFrame(users)
	# print(users_df.head())
	# users_df.to_csv('names/taskjam_users.csv', index=False)

	# with open('names/taskjam_users.json', 'w') as f:
	# 	json.dump(users, f, default=str)

def populate_db_users (collection):

	# users_df = pd.read_csv('names/taskjam_users.csv')	
	# users_df['json'] = users_df.apply(lambda x: x.to_json(), axis=1)
	# json_users = [json.loads(x) for x in users_df['json'].tolist()]
	# print((json_users[0]))

	with open('names/taskjam_users.json', 'r') as f:
		s = f.read()
		json_users = json.loads(s)
	for user in json_users:
		user['date_of_birth'] = datetime.strptime(user['date_of_birth'], '%Y-%m-%d %H:%M:%S')
		user['_id'] = user['username']
	# print(json_users[:2])
	collection.insert_many(json_users)


if __name__ == '__main__':


	# import pymongo

	# client = pymongo.MongoClient("mongodb+srv://oscargomezq:oscargomezq@cluster-taskjam-ahyms.mongodb.net/test?retryWrites=true&w=majority")
	# db = client["taskjam-db"]

	# populate_db_users(db.users_big)

	# populate_user_collection(db.users_big)

	pass