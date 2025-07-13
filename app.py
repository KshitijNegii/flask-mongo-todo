from flask import Flask, render_template, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

app = Flask(__name__)

# MongoDB Atlas connection
uri = "mongodb+srv://Kshitij:Iwillbe2004@cluster0.plxegn8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["todo_db"]
collection = db["todo_items"]

@app.route("/", methods=["GET", "POST"])
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        try:
            item = request.form.get("item")
            description = request.form.get("description")
            collection.insert_one({"item": item, "description": description})
            return render_template("success.html")
        except Exception as e:
            return render_template("form.html", error=str(e))
    return render_template("form.html")

@app.route("/api")
def api():
    with open("data.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

