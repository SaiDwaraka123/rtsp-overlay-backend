# app.py
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/rtsp_overlay_db")
PORT = int(os.getenv("PORT", 5000))

client = MongoClient(MONGO_URI)
db = client.get_database()
overlays_col = db["overlays"]

app = Flask(__name__)
CORS(app)

def serialize_overlay(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@app.route("/api/overlays", methods=["POST"])
def create_overlay():
    data = request.json
    res = overlays_col.insert_one(data)
    return jsonify({"message": "created", "id": str(res.inserted_id)}), 201

@app.route("/api/overlays", methods=["GET"])
def list_overlays():
    docs = list(overlays_col.find())
    docs = [serialize_overlay(d) for d in docs]
    return jsonify(docs), 200

@app.route("/api/overlays/<overlay_id>", methods=["GET"])
def get_overlay(overlay_id):
    doc = overlays_col.find_one({"_id": ObjectId(overlay_id)})
    if not doc:
        return jsonify({"message": "not found"}), 404
    return jsonify(serialize_overlay(doc)), 200

@app.route("/api/overlays/<overlay_id>", methods=["PUT"])
def update_overlay(overlay_id):
    data = request.json
    res = overlays_col.update_one({"_id": ObjectId(overlay_id)}, {"$set": data})
    if res.matched_count == 0:
        return jsonify({"message": "not found"}), 404
    return jsonify({"message": "updated"}), 200

@app.route("/api/overlays/<overlay_id>", methods=["DELETE"])
def delete_overlay(overlay_id):
    res = overlays_col.delete_one({"_id": ObjectId(overlay_id)})
    if res.deleted_count == 0:
        return jsonify({"message": "not found"}), 404
    return jsonify({"message": "deleted"}), 200

@app.route("/api/config", methods=["GET", "POST"])
def config():
    if request.method == "GET":
        cfg = db["config"].find_one({})
        if cfg:
            cfg["_id"] = str(cfg["_id"])
        return jsonify(cfg or {}), 200
    else:
        data = request.json
        db["config"].replace_one({}, data, upsert=True)
        return jsonify({"message": "saved"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
