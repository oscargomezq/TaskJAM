import pymongo

def add_user (collection, user):
	
	# Parse user json info
	user = user

	collection.insert_one(user)
