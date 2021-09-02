import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for the diffrent users
users = [
    {'name': 'logistics'}
    {'name': 'customer'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/api/v1/balance', methods=['POST'])
def api_balance():
    if 'name' in request.args:
        name = str(request.args['name'])
    else: 
        return "Error: No name field provided. Please specify a name."

@app.route('/api/v1/fund', methods=['POST'])
def api_fund():

@app.route('/api/v1/refund', methods=['POST'])
def api_refund():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."


    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
