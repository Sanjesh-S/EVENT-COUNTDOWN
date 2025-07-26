from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)

# Secure MongoDB URI from .env
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["event_db"]
events = db["events"]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index.html")
def index():
    return render_template("index.html")



@app.route("/event/<event_id>")
def view_event(event_id):
    return render_template("event.html")

@app.route("/api/create", methods=["POST"])
def create_event():
    data = request.json
    event = {
        "name": data["name"],
        "timezone": data["timezone"],
        "utc": data["utc"],
        "redirect": data["redirect"],
        "logo": data.get("logo")
    }
    result = events.insert_one(event)
    return jsonify({"id": str(result.inserted_id)})

@app.route("/api/event/<event_id>")
def get_event(event_id):
    event = events.find_one({"_id": ObjectId(event_id)})
    if not event:
        return jsonify({"error": "Event not found"}), 404

    return jsonify({
        "name": event["name"],
        "timezone": event["timezone"],
        "utc": event["utc"],
        "redirect": event["redirect"],
        "logo": event.get("logo")
    })

if __name__ == "__main__":
    app.run(debug=True)
