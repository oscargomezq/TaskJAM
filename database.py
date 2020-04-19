import pymongo

# user is a python dict
def add_user (collection, user):
	
	# Parse user json info

	# Insert to db
	collection.insert_one(user)

	try:
		return "Succesfully registered user " + user['first_name'] + " " + user['last_name']
	except:
		return "Error registering user"
