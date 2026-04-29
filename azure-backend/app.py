from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*", methods=["GET", "POST", "OPTIONS"])

@app.route('/api/message', methods=['GET', 'OPTIONS'])
def message():
    response = jsonify({"message": "Hello from Azure ☁️"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)