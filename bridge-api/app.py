from flask import Flask, request
from flask_cors import CORS
from process_data import add_db, get_db, delete_db

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	return f"Hello, world"

@app.route('/data', methods=['POST'])
def PostData():
    payload = request.get_json()
    return add_db(payload)

@app.route('/data', methods=['GET'])
def GetData():
    id = request.args.get('id')
    return get_db(id)

@app.route('/data', methods=['DELETE'])
def DeleteData():
    id = request.args.get('id')
    return delete_db(id)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    # app.run(debug=True)