import os
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# --- Database Setup ---
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["myapp"]
users_collection = db["users"]


# --- Database Logic Functions ---
def insert_user(name: str, age: int) -> str:
    result = users_collection.insert_one({"name": name, "age": age})
    return str(result.inserted_id)


def get_all_names() -> list[str]:
    # Returns a list of strings (names only)
    return [doc["name"] for doc in users_collection.find({}, {"name": 1, "_id": 0})]


def get_all_users() -> list[dict]:
    # Returns the full user objects (excluding MongoDB _id)
    return list(users_collection.find({}, {"_id": 0}))


# --- Flask Routes ---
@app.route("/")
def index():
    try:
        names = get_all_names()
        return render_template("index.html", names=names)
    except Exception as e:
        return f"Error connecting to database: {e}", 500



@app.route("/add", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name", "").strip()
    age = data.get("age")

    if not name or age is None:
        return jsonify({"error": "Name and age are required"}), 400

    try:
        insert_user(name, int(age))
        return jsonify(
            {"message": f"Successfully inserted: {name}", "names": get_all_names()}
        )
    except Exception as e:
        return jsonify({"error": f"Database error: {e}"}), 500


if __name__ == "__main__":
    # This starts the Flask web server
    app.run(debug=True)
