# Testing

# import pandas as pd
from flask import Flask, jsonify, request, render_template
# import pickle

# load model
# model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/testpost', methods=['POST'])
def postreq():
	if request.method == "POST":
		ret_dict = {"value": "YAY worked"}
		return jsonify(**ret_dict)
	# 	create_post(name,post)

	# posts = get_posts()
	# print("POST REQ")


# def predict():
#     # get data
#     data = request.get_json(force=True)

#     # convert data into dataframe
#     data.update((x, [y]) for x, y in data.items())
#     data_df = pd.DataFrame.from_dict(data)

#     # predictions
#     result = model.predict(data_df)

#     # send back to browser
#     output = {'results': int(result[0])}

#     # return data
#     return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)