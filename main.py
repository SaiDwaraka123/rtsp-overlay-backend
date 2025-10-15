# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# CORS
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["overlay_db"]
collection = db["overlays"]

@app.get("/")
def read_root():
    return {"message": "Backend is running successfully"}

# CRUD Routes
@app.post("/api/overlays")
def create_overlay(data: dict):
    res = collection.insert_one(data)
    return {"message": "Overlay created", "id": str(res.inserted_id)}

@app.get("/api/overlays")
def get_overlays():
    overlays = list(collection.find())
    for overlay in overlays:
        overlay["_id"] = str(overlay["_id"])
    return overlays

@app.put("/api/overlays/{overlay_id}")
def update_overlay(overlay_id: str, data: dict):
    result = collection.update_one({"_id": ObjectId(overlay_id)}, {"$set": data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Overlay not found")
    return {"message": "Overlay updated"}

@app.delete("/api/overlays/{overlay_id}")
def delete_overlay(overlay_id: str):
    result = collection.delete_one({"_id": ObjectId(overlay_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Overlay not found")
    return {"message": "Overlay deleted"}


# from fastapi import FastAPI
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from fastapi.middleware.cors import CORSMiddleware
# import os

# load_dotenv()

# app = FastAPI()

# origins = [
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,  # or ["*"] for all
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # MongoDB connection
# MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
# client = MongoClient(MONGO_URI)
# db = client["overlay_db"]
# collection = db["overlays"]

# @app.get("/")
# def read_root():
#     return {"message": "Backend is running successfully"}

# @app.post("/overlay")
# def create_overlay(data: dict):
#     collection.insert_one(data)
#     return {"message": "Overlay data saved successfully"}

# @app.get("/overlay")
# def get_overlays():
#     overlays = list(collection.find({}, {"_id": 0}))
#     return overlays
