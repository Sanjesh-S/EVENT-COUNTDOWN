from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import shortuuid
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Read MongoDB URI from environment variable
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["event_countdowns"]
events = db["events"]

@app.route('/api/create', methods=['POST'])
def create_event():
    data = request.json
    name = data.get("name")
    timezone = data.get("timezone")
    utc = data.get("utc")
    redirect = data.get("redirect")
    logo = data.get("logo")

    if not name or not timezone or not utc or not redirect:
        return jsonify({"error": "Missing fields"}), 400

    short_code = shortuuid.uuid()[:6]

    event = {
        "name": name,
        "timezone": timezone,
        "utc": utc,
        "redirect": redirect,
        "logo": logo,
        "short_code": short_code,
        "created_at": datetime.utcnow()
    }

    events.insert_one(event)
    return jsonify({"short_code": short_code}), 201

@app.route('/api/event/<short_code>', methods=['GET'])
def get_event(short_code):
    event = events.find_one({"short_code": short_code}, {"_id": 0})
    if not event:
        return jsonify({"error": "Not found"}), 404
    return jsonify(event)

@app.route('/event/<short_code>')
def serve_event_with_code(short_code):
    return send_from_directory('.', 'event.html')

@app.route('/event.html')
def serve_event_page():
    return send_from_directory('.', 'event.html')

@app.route('/index.html')
def serve_index_page():
    return send_from_directory('.', 'index.html')

@app.route('/')
def serve_home():
    return send_from_directory('.', 'home.html')

if __name__ == '__main__':
    app.run(debug=True)
